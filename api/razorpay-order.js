export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { amount } = req.body; // amount in INR
  
  // Use environment variables in production, fallback to provided live keys for dev
  const rzpKey = process.env.RAZORPAY_KEY_ID || 'rzp_live_ThKViVSs1B9jNs';
  const rzpSecret = process.env.RAZORPAY_KEY_SECRET || 'WE5oemjmrh9BPUHDaYh0fcUw';

  try {
    const response = await fetch('https://api.razorpay.com/v1/orders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + Buffer.from(rzpKey + ':' + rzpSecret).toString('base64')
      },
      body: JSON.stringify({
        amount: Math.round(amount * 100), // convert INR to paise
        currency: 'INR',
        receipt: 'rcpt_' + Date.now().toString()
      })
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error?.description || 'Razorpay order failed');
    }
    
    res.status(200).json(data);
  } catch (e) {
    console.error('Razorpay Order Error:', e);
    res.status(500).json({ error: e.message });
  }
}
