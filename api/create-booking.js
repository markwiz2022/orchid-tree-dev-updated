export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const API_KEY = process.env.STAYFLEXI_API_KEY || 'ea80f9224c59ded5969d';
  const HOTEL_ID = '25068';

  const { checkin, checkout, adults, children, guestName, guestPhone, guestEmail, roomIds, subtotal } = req.body;

  const totalGuests = (parseInt(adults) || 0) + (parseInt(children) || 0);
  if (totalGuests > 34) {
    return res.status(400).json({ error: 'Orchid Tree accommodates a maximum of 34 overnight guests.' });
  }

  // Map our logical room categories to Stayflexi roomTypeIds
  const typeMap = {
    'bael': '12370', 'bilva': '12370', 'datura': '12370', 'tulsi': '12370',
    'hattimara': '12371', 'bodhi-tree': '12371',
    'ashoka': '12372', 'mallige': '12372', 'parijata': '12372', 'spatika': '12372',
    'chandana': '12373'
  };

  // Build roomStays array
  const roomStays = (roomIds || []).map(id => ({
    numAdults: Math.max(1, Math.floor(adults / roomIds.length)),
    numChildren: Math.floor((children || 0) / roomIds.length),
    numChildren1: 0,
    roomTypeId: typeMap[id] || '12370',
    ratePlanId: "30251" // Default standard rate plan for now
  }));

  // Helper to convert YYYY-MM-DD to DD-MM-YYYY
  const formatSfDate = (dateStr, timeStr) => {
    if (!dateStr) return "";
    const parts = dateStr.split('-');
    if (parts.length === 3) {
      return `${parts[2]}-${parts[1]}-${parts[0]} ${timeStr}`;
    }
    return `${dateStr} ${timeStr}`;
  };

  const payload = {
    checkin: formatSfDate(checkin, "13:00:00"),
    checkout: formatSfDate(checkout, "11:00:00"),
    hotelId: HOTEL_ID,
    bookingStatus: "CONFIRMED",
    bookingSource: "STAYFLEXI_OD",
    roomStays: roomStays,
    customerDetails: {
      firstName: guestName ? guestName.split(' ')[0] : "Guest",
      lastName: guestName && guestName.includes(' ') ? guestName.split(' ').slice(1).join(' ') : "",
      emailId: guestEmail || "test@test.com",
      phoneNumber: guestPhone || "+919999999999"
    },
    paymentDetails: {
      sellRate: subtotal || 0,
      roomRate: subtotal || 0,
      payAtHotel: false
    },
    requestToBook: false,
    isAddOnPresent: false,
    isInsured: false,
    isEnquiry: true, // MUST BE TRUE for Pay-Now flows to wait for payment
    isExternalPayment: false
  };

  const url = `https://api.stayflexi.com/core/api/v1/beservice/perform-booking`;

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'X-SF-API-KEY': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Stayflexi Booking Error:', errorText);
      return res.status(response.status).json({ error: 'Stayflexi API error', details: errorText });
    }

    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    console.error('API Fetch Error:', error);
    return res.status(500).json({ error: 'Internal Server Error', details: error.message });
  }
}
