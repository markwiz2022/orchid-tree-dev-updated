export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const API_KEY = process.env.STAYFLEXI_API_KEY || 'ea80f9224c59ded5969d';
  const HOTEL_ID = '25068';
  const { bookingId, paymentId, amount } = req.body;

  const url = 'https://api.stayflexi.com/api/v2/payments/recordExternalPayment/';

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'X-SF-API-KEY': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        hotel_id: HOTEL_ID,
        booking_id: bookingId,
        booking_source: "CUSTOM_BE",
        module_source: "CUSTOM_BE_PAYMENT",
        amount: amount,
        currency: "INR",
        payment_gateway_id: paymentId,
        pg_name: "RAZORPAY",
        requires_post_payment_confirmation: "true",
        payment_type: "Razorpay Online",
        payment_issuer: "Razorpay",
        payment_mode: "ONLINE",
        status: "SUCCESS"
      })
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Stayflexi Payment Record Error:', errorText);
      return res.status(response.status).json({ error: 'Stayflexi API error', details: errorText });
    }

    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    console.error('API Fetch Error:', error);
    return res.status(500).json({ error: 'Internal Server Error', details: error.message });
  }
}
