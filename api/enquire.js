import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method Not Allowed' });
  }

  const { message } = req.body;
  const user = process.env.SMTP_USER || 'orchidtree.blr@gmail.com';
  const pass = process.env.SMTP_PASS;

  if (!pass) {
    console.error('SMTP_PASS is missing in environment variables. Cannot send email.');
    return res.status(500).json({ success: false, message: 'SMTP credentials not configured on server.' });
  }

  try {
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: user,
        pass: pass
      }
    });

    const mailOptions = {
      from: user,
      to: 'orchidtree.blr@gmail.com',
      subject: 'New Enquiry from Orchid Tree Website',
      text: message || 'An enquiry was submitted without details.'
    };

    await transporter.sendMail(mailOptions);
    return res.status(200).json({ success: true, message: 'Enquiry submitted successfully.' });
  } catch (error) {
    console.error('Error sending email:', error);
    return res.status(500).json({ success: false, message: 'Email dispatch failed.' });
  }
}