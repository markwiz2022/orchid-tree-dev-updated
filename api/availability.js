export default async function handler(req, res) {
  const { checkin, checkout } = req.query;

  if (!checkin || !checkout) {
    return res.status(400).json({ error: 'Missing checkin or checkout dates' });
  }

  // Using environment variable for production, with the test key as fallback for this dev phase
  const API_KEY = process.env.STAYFLEXI_API_KEY || 'ea80f9224c59ded5969d';
  const HOTEL_ID = '25068';

  const formatSfDate = (dateStr, timeStr) => {
    if (!dateStr) return "";
    const parts = dateStr.split('-');
    if (parts.length === 3) {
      return `${parts[2]}-${parts[1]}-${parts[0]} ${timeStr}`;
    }
    return `${dateStr} ${timeStr}`;
  };

  const sfCheckin = formatSfDate(checkin, "13:00:00");
  const sfCheckout = formatSfDate(checkout, "11:00:00");

  const url = `https://api.stayflexi.com/core/api/v1/beservice/hoteldetailadvanced?hotelId=${HOTEL_ID}&checkin=${encodeURIComponent(sfCheckin)}&checkout=${encodeURIComponent(sfCheckout)}&discount=0`;

  try {
    const response = await fetch(url, {
      headers: {
        'X-SF-API-KEY': API_KEY,
        'Accept': 'application/json'
      }
    });

    if (!response.ok) {
      const errorText = await response.text();
      return res.status(response.status).json({ error: 'Stayflexi API error', details: errorText });
    }

    const sfData = await response.json();

    // Map Stayflexi IDs to our logical types
    const typeMap = {
      '12370': 'Couple Room by the Pool',
      '12371': 'Couple Garden Cottage',
      '12372': 'Family Room by the Pool',
      '12373': 'Family Garden Cottage'
    };

    // Calculate approx occupancy key (e.g. "2+1") based on request
    const a = Math.max(1, parseInt(req.query.adults) || 2);
    const c = parseInt(req.query.children) || 0;
    // Just a rough guess for now: if someone asks for 4 adults, a room might hold 2. We check "2", "2+1" etc.
    // For simplicity, we just return the minimum rate available for 1 or 2 adults to show base pricing.
    
    const liveData = {};
    if (sfData && sfData.roomTypeMap) {
      for (const sfId in sfData.roomTypeMap) {
        if (typeMap[sfId]) {
          const typeName = typeMap[sfId];
          const roomData = sfData.roomTypeMap[sfId];
          
          let availableRooms = 0;
          let availableIds = [];
          let baseRate = 0;
          
          if (roomData.combos && roomData.combos.length > 0) {
            // First combo represents the check-in to check-out period
            const combo = roomData.combos[0];
            availableRooms = combo.availableRooms || 0;
            // Parse onlineRoomIds to get names (e.g., "Ashoka Parijatha")
            if (combo.onlineRoomIds && typeof combo.onlineRoomIds === 'string') {
              availableIds = combo.onlineRoomIds.split(' ').map(s => s.trim().toLowerCase().replace('bodhitree', 'bodhi-tree').replace('parijatha', 'parijata'));
            } else if (Array.isArray(combo.onlineRoomIds)) {
              availableIds = combo.onlineRoomIds.map(s => s.toLowerCase().replace('bodhitree', 'bodhi-tree').replace('parijatha', 'parijata'));
            }
            
            // Get rate for 2 adults as baseline
            if (combo.rates && combo.rates.length > 0) {
              const rateObj = combo.rates[0];
              if (rateObj.priceMap && rateObj.priceMap["2"]) {
                baseRate = rateObj.priceMap["2"];
                // optionally add taxes if needed, but our UI says "pre-tax"
              } else if (rateObj.priceMap && rateObj.priceMap["1"]) {
                baseRate = rateObj.priceMap["1"];
              }
            }
          }
          
          liveData[typeName] = {
            count: availableRooms,
            roomIds: availableIds, // e.g. ["ashoka", "parijata"]
            price: baseRate
          };
        }
      }
    }

    return res.status(200).json(liveData);
  } catch (error) {
    console.error('API Fetch Error:', error);
    return res.status(500).json({ error: 'Internal Server Error', details: error.message });
  }
}
