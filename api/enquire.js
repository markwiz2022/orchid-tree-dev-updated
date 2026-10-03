export default async function handler(req, res) {
  if (req.method === 'POST') {
    console.log('Enquiry received:', req.body);
    // In production, wire this to Nodemailer, SendGrid, or AWS SES
    res.status(200).json({ success: true, message: 'Enquiry submitted successfully.' });
  } else {
    res.status(405).json({ message: 'Method Not Allowed' });
  }
}