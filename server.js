import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';

// Load environment variables if present
dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// API Route Handlers (Imported from our Vercel functions)
import availabilityHandler from './api/availability.js';
import createBookingHandler from './api/create-booking.js';
import razorpayOrderHandler from './api/razorpay-order.js';
import confirmPaymentHandler from './api/confirm-payment.js';

app.all('/api/availability', availabilityHandler);
app.all('/api/create-booking', createBookingHandler);
app.all('/api/razorpay-order', razorpayOrderHandler);
app.all('/api/confirm-payment', confirmPaymentHandler);

// Serve Static Frontend Files
app.use(express.static(__dirname));

// Fallback for HTML routing
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log('Ensure you are running this with PM2 or a Node.js process manager on your VPS.');
});
