export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { token } = req.body;
  const secretKey = process.env.RECAPTCHA_SECRET_KEY || '6LcfodMtAAAAAB7WGpV01p4kSBdnWEO78CGD6Yud';

  try {
    const response = await fetch('https://www.google.com/recaptcha/api/siteverify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: `secret=${secretKey}&response=${token}`
    });
    
    const data = await response.json();
    
    if (data.success) {
      res.status(200).json({ success: true });
    } else {
      res.status(400).json({ success: false, error: 'reCAPTCHA verification failed', details: data });
    }
  } catch (e) {
    console.error('reCAPTCHA Error:', e);
    res.status(500).json({ error: e.message });
  }
}
