import os

f = 'host-with-us.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old_btns = '''<div class="btns">
            <a class="cta primary" href="https://wa.me/918088251913?text=Hi%20Orchid%20Tree%2C%20we%27d%20like%20to%20host%20a%20gathering.%20Type%3A%20___.%20Preferred%20dates%3A%20___.%20Guests%3A%20___." target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.7 4.8-1.3A10 10 0 1 0 12 2zm5.2 14.1c-.2.6-1.2 1.1-1.7 1.2-.4.1-1 .1-1.6-.1-.4-.1-.9-.3-1.5-.5-2.6-1.1-4.3-3.8-4.5-4-.1-.2-1-1.4-1-2.6 0-1.2.6-1.8.9-2.1.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5.2.5.7 1.7.7 1.8.1.1.1.3 0 .4l-.3.5c-.1.2-.3.4-.1.7.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.2.1.4.1.5-.1l.7-.8c.2-.2.4-.2.6-.1l1.6.8c.2.1.4.2.5.3.1.2.1.5-.1 1z"/></svg>
              Plan on WhatsApp</a>
            <a class="cta ghost" href="mailto:orchidtree.blr@gmail.com?subject=Hosting%20enquiry&body=Hi%20Orchid%20Tree%2C%20we%27d%20like%20to%20host%20a%20gathering.%20Type%3A%20.%20Preferred%20dates%3A%20.%20Guests%3A%20.">
              Email us</a>
          </div>'''

new_btns = '''
        <form class="enquiry-card" id="enqForm" novalidate style="box-shadow:none; padding: 24px 0 0; background:transparent; border:none; margin:0;">
          <div class="two">
            <div class="field">
              <label for="enqName">Name</label>
              <input type="text" id="enqName" name="name" placeholder="Who we will be planning with">
            </div>
            <div class="field">
              <label for="enqEmailIn">Email</label>
              <input type="email" id="enqEmailIn" name="email" placeholder="Your email">
            </div>
          </div>
          <div class="two">
            <div class="field">
              <label for="enqType">Gathering type</label>
              <input type="text" id="enqType" name="type" placeholder="What you are hosting">
            </div>
            <div class="field">
              <label for="enqDate">Preferred dates</label>
              <input type="text" id="enqDate" name="date" placeholder="A month or a week, say">
            </div>
          </div>
          <div class="field">
            <label for="enqGuests">Guests</label>
            <input type="text" id="enqGuests" name="guests" placeholder="Roughly how many">
          </div>
          <button type="submit" class="enquiry-submit cta primary" style="border:none; cursor:pointer;">
            Send Enquiry
          </button>
        </form>
'''

c = c.replace(old_btns, new_btns)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
