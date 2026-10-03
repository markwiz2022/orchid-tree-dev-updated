
  (function(){
    const S = window.OrchidStore, C = window.OrchidCatalog, CT = window.OrchidContent;

    // ---- small helpers ---------------------------------------------------
    function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
    function waLink(num, msg){ return num ? 'https://wa.me/'+num+'?text='+encodeURIComponent(msg) : '#'; }

    // simple inline line-icons (stroke = currentColor), used by the experiences band
    var ICONS = {
      paddle: '<circle cx="11" cy="9" r="6"/><line x1="8.5" y1="13.5" x2="6" y2="20"/>',
      board: '<rect x="4" y="4" width="16" height="16" rx="2"/><circle cx="12" cy="12" r="2.5"/>',
      dice: '<rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="9" cy="9" r="1.1" fill="currentColor" stroke="none"/><circle cx="15" cy="15" r="1.1" fill="currentColor" stroke="none"/><circle cx="15" cy="9" r="1.1" fill="currentColor" stroke="none"/><circle cx="9" cy="15" r="1.1" fill="currentColor" stroke="none"/>',
      trampoline: '<ellipse cx="12" cy="9" rx="8" ry="3"/><line x1="6" y1="11" x2="4.5" y2="19"/><line x1="18" y1="11" x2="19.5" y2="19"/>',
      mic: '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M6 11a6 6 0 0 0 12 0"/><line x1="12" y1="17" x2="12" y2="21"/>',
      music: '<circle cx="7" cy="18" r="2.3"/><circle cx="17" cy="16" r="2.3"/><path d="M9.3 18V6l10-2v10"/>',
      film: '<rect x="3" y="5" width="18" height="14" rx="2"/><line x1="7.5" y1="5" x2="7.5" y2="19"/><line x1="16.5" y1="5" x2="16.5" y2="19"/>',
      fire: '<path d="M12 3c.5 3 3.5 4 3.5 8a3.5 3.5 0 0 1-7 0c0-1.5.8-2.5 1.7-3.3.2 1.6 1.8 1.6 1.8 0 0-1.8 0-3 0-4.7z"/>',
      star: '<path d="M12 3.5l2.5 5.5 6 .5-4.5 4 1.4 5.8L12 21.4 6.6 19.3 8 13.5l-4.5-4 6-.5z"/>',
      leaf: '<path d="M5 19c0-8 6-14 14-14 0 8-6 14-14 14z"/><line x1="5" y1="19" x2="12.5" y2="11.5"/>',
      car: '<path d="M4 13l1.8-5h12.4L20 13"/><path d="M3 17v-4h18v4h-2"/><path d="M3 17h2"/><path d="M19 17h2"/><circle cx="7.5" cy="17.5" r="1.8"/><circle cx="16.5" cy="17.5" r="1.8"/>',
      binoculars: '<circle cx="7" cy="15" r="3.2"/><circle cx="17" cy="15" r="3.2"/><path d="M7 12l1-5h2.5l.6 4"/><path d="M17 12l-1-5h-2.5l-.6 4"/><line x1="10.2" y1="15" x2="13.8" y2="15"/>',
      trail: '<path d="M3 19l5.5-10 3.5 6 2-3 7 7z"/>',
      ball: '<circle cx="12" cy="12" r="9"/><path d="M12 7.2l3.4 2.5-1.3 4h-4.2l-1.3-4z"/><path d="M12 3v4.2M4.2 9.6l4.5 2.1M19.8 9.6l-4.5 2.1M7.6 20.2l2.3-6.5M16.4 20.2l-2.3-6.5"/>',
      volley: '<circle cx="12" cy="12" r="9"/><path d="M12 3c3 4 3.6 12-1.4 17.8"/><path d="M3.4 9.4c4.8-.4 11 2.8 13.4 9.4"/><path d="M20.8 13.6c-3.6-2.6-10.6-3-15.6 1.6"/>',
      cricket: '<path d="M14.5 3.6l5.9 5.9-8.6 8.6-5.9-5.9z"/><line x1="5.9" y1="12.2" x2="3.4" y2="14.7"/><circle cx="18.6" cy="18.6" r="2.4"/>',
      tree: '<path d="M12 3c3.4 0 6 2.4 6 5.4 0 3-2.6 5.4-6 5.4s-6-2.4-6-5.4C6 5.4 8.6 3 12 3z"/><line x1="12" y1="13.8" x2="12" y2="21"/><path d="M9 21c0-2.4 1.2-3.6 3-3.6s3 1.2 3 3.6"/><line x1="8.6" y1="12.4" x2="8.6" y2="21"/><line x1="15.4" y1="12.4" x2="15.4" y2="21"/>',
      fork: '<path d="M7 3v6a2.5 2.5 0 0 0 5 0V3"/><line x1="9.5" y1="9" x2="9.5" y2="21"/><path d="M17.5 3c-1.4 1.6-2 3.4-2 5.4 0 1.6.7 2.6 2 3.1V21"/>',
      dot: '<circle cx="12" cy="12" r="3" fill="currentColor" stroke="none"/>',
    };
    function iconSvg(key){
      var p = ICONS[key] || ICONS.dot;
      return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>';
    }
    function stars(n){ var f=Math.round(n), s=''; for(var i=0;i<5;i++) s+= i<f ? '★' : '☆'; return s; }
    // apply a real photo to a placeholder .media div (keeps textured fallback when null)
    function applyImg(id, url){
      var el=document.getElementById(id); if(!el) return;
      if(url){ el.classList.remove('dark'); el.style.background="#e7e1d4 url('"+url+"') center/cover no-repeat"; }
    }
    // build a .media div as an HTML string, with optional photo + extra style
    function mediaHtml(url, extra){
      if(url) return '<div class="media" style="background:#e7e1d4 url(\''+esc(url)+'\') center/cover no-repeat;'+(extra||'')+'"></div>';
      return '<div class="media dark"'+(extra?' style="'+extra+'"':'')+'></div>';
    }
    // a calm review block (returns '' if no review at this slot)
    function reviewHtml(id){
      if(!id) return '';
      var r = CT.getReview(id); if(!r) return '';
      var rateLink = CT.googleReviewsUrl
        ? '<a class="stars" href="'+esc(CT.googleReviewsUrl)+'" target="_blank" rel="noopener" title="'+r.rating+' out of 5">'+stars(r.rating)+'</a>'
        : '<span class="stars" title="'+r.rating+' out of 5">'+stars(r.rating)+'</span>';
      return '<div class="review"><div class="q">“'+esc(r.text)+'”</div>'+
        '<div class="meta"><span class="nm">'+esc(r.name)+'</span>'+
        (r.verified?'<span class="vg">Verified Guest</span>':'')+rateLink+'</div></div>';
    }

    // ---- resolve booking from ?b=<token> ----
    const token = new URLSearchParams(location.search).get('b');
    let booking = token ? S.getByToken(token) : null;

    if(!booking){
      document.getElementById('notfound').style.display = 'flex';
      return;
    }

    // mark viewed (no-op if already confirmed/declined)
    S.markViewed(booking.id);
    booking = S.getById(booking.id);

    document.getElementById('page').style.display = 'block';

    // expose modal handlers globally (markup uses onclick)
    window.openRoom = function(id){
      const r = C.get(id); if(!r) return;
      document.getElementById('mCat').textContent = r.category;
      document.getElementById('mTitle').textContent = r.name;
      document.getElementById('mTagline').innerHTML = esc(r.tagline)+(r.tier?'<span class="tier">'+esc(r.tier)+'</span>':'');
      document.getElementById('mStory').textContent = r.story || '';
      document.getElementById('mDesc').textContent = r.description || '';

      // price line only when a real price exists (3 of 4 types have none)
      var priceEl = document.getElementById('mPrice');
      if(r.priceFrom){ priceEl.style.display=''; priceEl.textContent = 'From '+S.rupees(r.priceFrom)+' + taxes. Room and massage.'; }
      else { priceEl.style.display='none'; }

      // gallery: auto-advancing crossfade + prev/next + thumbnails
      var urls = roomUrls(r);
      mgStart(urls);

      // specs grid
      document.getElementById('mFacts').innerHTML = (r.facts || []).map(function(f){
        return '<div class="f"><span class="k">'+esc(f.label)+'</span><span class="v">'+esc(f.value)+'</span></div>';
      }).join('');

      // what this place offers — the full per-type amenity list from the site
      document.getElementById('mOffers').innerHTML = (r.amenities || []).map(function(a){ return '<span class="a">'+esc(a)+'</span>'; }).join('');

      // ask about this specific room
      var num = CT.contact && CT.contact.whatsapp;
      document.getElementById('mAsk').innerHTML = num
        ? '<a class="room-ask" href="'+esc(waLink(num, "Hi, I have a question about the "+r.name+" room at Orchid Tree."))+'" target="_blank" rel="noopener">Have a question about this room? Message us &rarr;</a>'
        : '';

      document.getElementById('overlay').classList.add('open');
    };
    window.closeModal = function(){ mgStop(); document.getElementById('overlay').classList.remove('open'); };

    // terms and conditions modal (built from content.terms)
    window.openTerms = function(){
      var t = CT.terms || { sections: [] };
      document.getElementById('termsBody').innerHTML = t.sections.map(function(s){
        return '<div class="terms-sec"><div class="ts-title">'+esc(s.title)+'</div><ul>'+
          s.items.map(function(i){ return '<li>'+esc(i)+'</li>'; }).join('')+'</ul></div>';
      }).join('');
      document.getElementById('termsOverlay').classList.add('open');
    };
    window.closeTerms = function(){ document.getElementById('termsOverlay').classList.remove('open'); };

    // ---- modal gallery: auto-advance crossfade + manual prev/next ----------
    var MG = { urls: [], i: 0, cur: 0, timer: null };
    function mgLayers(){ return [document.querySelector('#mMain .rm-base'), document.querySelector('#mMain .rm-top')]; }
    function mgGo(target){
      var n = MG.urls.length; if(!n) return;
      target = (target + n) % n; MG.i = target;
      var layers = mgLayers(), incoming = layers[1 - MG.cur];
      incoming.style.backgroundImage = "url('" + MG.urls[target] + "')";
      incoming.style.opacity = '1';
      layers[MG.cur].style.opacity = '0';
      MG.cur = 1 - MG.cur;
      var cnt = document.getElementById('mCount'); if(cnt) cnt.textContent = (target + 1) + ' / ' + n;
      var thumbs = document.getElementById('mThumbs');
      if(thumbs){ var a = thumbs.querySelector('.th.active'); if(a) a.classList.remove('active');
        var t = thumbs.querySelector('.th[data-i="' + target + '"]'); if(t) t.classList.add('active'); }
    }
    function mgTimer(){ clearInterval(MG.timer); MG.timer = null; if(MG.urls.length > 1) MG.timer = setInterval(function(){ mgGo(MG.i + 1); }, 3200); }
    function mgStop(){ clearInterval(MG.timer); MG.timer = null; }
    function mgStart(urls){
      mgStop(); MG.urls = urls || []; MG.i = 0; MG.cur = 0;
      var layers = mgLayers();
      layers[0].style.backgroundImage = urls[0] ? "url('" + urls[0] + "')" : ''; layers[0].style.opacity = '1';
      layers[1].style.backgroundImage = ''; layers[1].style.opacity = '0';
      urls.forEach(function(u){ var im = new Image(); im.src = u; }); // preload
      var multi = urls.length > 1;
      document.getElementById('mPrev').style.display = multi ? '' : 'none';
      document.getElementById('mNext').style.display = multi ? '' : 'none';
      document.getElementById('mCount').style.display = multi ? '' : 'none';
      document.getElementById('mCount').textContent = '1 / ' + urls.length;
      // thumbnails
      var thumbs = document.getElementById('mThumbs');
      thumbs.innerHTML = multi
        ? urls.map(function(u, i){ return '<div class="th' + (i === 0 ? ' active' : '') + '" data-i="' + i + '" style="background-image:url(\'' + esc(u) + '\')"></div>'; }).join('')
        : '';
      Array.prototype.forEach.call(thumbs.querySelectorAll('.th'), function(th){
        th.addEventListener('click', function(){ mgGo(+th.getAttribute('data-i')); mgTimer(); });
      });
      mgTimer();
    }
    document.getElementById('mPrev').addEventListener('click', function(){ mgGo(MG.i - 1); mgTimer(); });
    document.getElementById('mNext').addEventListener('click', function(){ mgGo(MG.i + 1); mgTimer(); });

    function roomUrls(r){ return (r.imageUrls && r.imageUrls.length) ? r.imageUrls : (r.imageUrl ? [r.imageUrl] : []); }

    function band(r){
      var urls = roomUrls(r);
      var first = urls[0] || null;
      var baseLayer = first
        ? '<div class="rb-img rb-base" style="background-image:url(\''+esc(first)+'\')"></div>'
        : '<div class="media dark rb-base"></div>';
      var cue = urls.length > 1 ? '<div class="rb-cue"><span class="dot"></span>'+urls.length+' photos</div>' : '';
      // top-left "who fits here" cluster: occupancy + pet policy
      var occ = esc(r.occupancyShort || ('Sleeps ' + r.capacity));
      var petPill = r.petFriendly
        ? '<span class="rb-pill pet">Pets welcome</span>'
        : '<span class="rb-pill nopet">No pets</span>';
      var meta = '<div class="rb-meta"><span class="rb-pill">'+occ+'</span>'+petPill+'</div>';
      // bottom tags: feature highlights only
      var hi = (r.highlights && r.highlights.length ? r.highlights : [r.signature]).slice(0, 2)
        .map(function(h){ return '<span class="tag">'+esc(h)+'</span>'; }).join('');
      return ''+
      '<div class="room-band" data-room="'+esc(r.id)+'" onclick="openRoom(\''+r.id+'\')">'+
        baseLayer+
        '<div class="rb-img rb-top"></div>'+
        '<div class="scrim"></div>'+
        meta + cue +
        '<div class="cap">'+
          '<div class="rn">'+esc(r.name)+'</div>'+
          '<div class="rt">'+esc(r.tagline)+' · '+esc(r.category)+'</div>'+
          '<div class="tags">'+hi+'</div>'+
          '<span class="rb-btn">View room details <span class="arr">&rsaquo;</span></span>'+
        '</div>'+
      '</div>';
    }

    // inline room detail for the single-room layout (fills the left column,
    // mirrors the modal's description + specs + amenities)
    function roomDetailPanel(r){
      var facts = (r.facts || []).map(function(f){
        return '<div class="f"><span class="k">'+esc(f.label)+'</span><span class="v">'+esc(f.value)+'</span></div>';
      }).join('');
      var offers = (r.amenities || []).map(function(a){ return '<span class="a">'+esc(a)+'</span>'; }).join('');
      return '<div class="room-detail">'+
        '<p class="rd-desc">'+esc(r.description || '')+'</p>'+
        '<div class="facts">'+facts+'</div>'+
        '<div class="eyebrow" style="margin-top:24px;">What this place offers</div>'+
        '<div class="amen-list">'+offers+'</div>'+
      '</div>';
    }

    // on hover, gently crossfade through a room's gallery (two-layer ping-pong:
    // exactly one layer is visible at a time, so there is no flicker or reset jump);
    // return to the cover on leave.
    function attachRoomCarousels(){
      Array.prototype.forEach.call(document.querySelectorAll('.room-band'), function(el){
        var r = C.get(el.getAttribute('data-room')); if(!r) return;
        var urls = roomUrls(r); if(urls.length < 2) return;
        var layers = [el.querySelector('.rb-base'), el.querySelector('.rb-top')];
        if(!layers[0] || !layers[1]) return;
        var cur = 0, idx = 0, loaded = false;
        function bg(layer, url){ layer.style.backgroundImage = "url('"+url+"')"; }
        function preload(){ if(loaded) return; loaded = true; urls.forEach(function(u){ var im = new Image(); im.src = u; }); }
        function reset(){ bg(layers[0], urls[0]); layers[0].style.opacity = '1'; layers[1].style.opacity = '0'; cur = 0; idx = 0; }
        function advance(){
          if(!el._hover) return;
          idx = (idx + 1) % urls.length;
          var nxt = layers[1 - cur];
          bg(nxt, urls[idx]);
          nxt.style.opacity = '1';        // fade incoming in
          layers[cur].style.opacity = '0'; // fade current out (same .9s transition)
          cur = 1 - cur;
          el._t = setTimeout(advance, 2500); // ~0.9s fade + ~1.6s hold
        }
        el.addEventListener('mouseenter', function(){ el._hover = true; preload(); reset(); el._t = setTimeout(advance, 1100); });
        el.addEventListener('mouseleave', function(){ el._hover = false; clearTimeout(el._t); reset(); });
      });
    }

    // ---- render the whole page from the booking ----
    function render(){
      const rooms = S.rooms(booking);
      const roomCount = rooms.length;
      const guests = S.guestCount(booking);
      const nights = S.nights(booking);
      const mix = booking.guestMix;
      const pets = mix.pets;

      document.getElementById('welcomeLine').textContent = S.welcomeLine(booking);
      document.getElementById('heroDates').textContent = S.dateRangeLabel(booking);
      document.getElementById('rmplural').textContent = roomCount > 1 ? 's' : '';

      document.getElementById('summary').innerHTML =
        '<div><div class="n">'+guests+'</div><div class="t">Guests</div></div>'+
        '<div><div class="n">'+roomCount+'</div><div class="t">Room'+(roomCount>1?'s':'')+'</div></div>'+
        '<div><div class="n">'+nights+'</div><div class="t">Nights</div></div>'+
        '<div><div class="n">'+pets+'</div><div class="t">Pet'+(pets===1?'':'s')+'</div></div>';

      let chips = '<span class="chip"><b>'+mix.adults+'</b> adult'+(mix.adults===1?'':'s')+'</span>';
      if(mix.children>0) chips += '<span class="chip"><b>'+mix.children+'</b> '+(mix.children===1?'child':'children')+'</span>';
      if(pets>0) chips += '<span class="chip"><b>'+pets+'</b> pet'+(pets===1?'':'s')+'</span>';
      document.getElementById('mix').innerHTML = chips;

      const area = document.getElementById('roomsArea');
      document.getElementById('groupLine').textContent = S.groupLine(booking);
      if(roomCount === 1){
        // single room: the left column would otherwise be short next to the tall
        // booking card, so surface the room's full detail inline to balance it
        area.className = 'room-hero';
        area.innerHTML = band(rooms[0]) + roomDetailPanel(rooms[0]);
      } else {
        area.className = '';
        area.innerHTML = rooms.map(band).join('');
      }
      attachRoomCarousels();

      // booking-for (collect + verify details here when missing)
      renderGuestBlock();
      document.getElementById('gDates').textContent = S.dateRangeLabel(booking);

      // invoice (shows the usual price struck by a discount when one is set)
      const subtotal = booking.pricing.roomSubtotal;
      const roomsLbl = roomCount+' room'+(roomCount>1?'s':'')+', '+nights+' night'+(nights===1?'':'s');
      var invoice;
      if(S.discount(booking) > 0){
        invoice =
          '<div class="row"><span>'+roomsLbl+'</span><span>'+S.rupees(S.listPrice(booking))+'</span></div>'+
          '<div class="row save"><span>You save ('+S.discountPct(booking)+'% off)</span><span>- '+S.rupees(S.discount(booking))+'</span></div>'+
          '<div class="row"><span>Taxes (18%)</span><span>'+S.rupees(S.tax(booking))+'</span></div>'+
          '<div class="row total"><span>Total</span><span>'+S.rupees(S.grandTotal(booking))+'</span></div>';
      } else {
        invoice =
          '<div class="row"><span>'+roomsLbl+'</span><span>'+S.rupees(subtotal)+'</span></div>'+
          '<div class="row"><span>Taxes (18%)</span><span>'+S.rupees(S.tax(booking))+'</span></div>'+
          '<div class="row total"><span>Total</span><span>'+S.rupees(S.grandTotal(booking))+'</span></div>';
      }
      document.getElementById('totalRows').innerHTML = invoice;
      document.getElementById('mobileAmt').textContent = S.rupees(S.grandTotal(booking));

      // food credit — hide the invoice card and the food-band overlay when zero
      const hasFood = booking.foodCredit > 0;
      document.getElementById('foodCreditCard').style.display = hasFood ? '' : 'none';
      document.getElementById('foodCap').style.display = hasFood ? '' : 'none';
      if(hasFood){
        document.getElementById('foodAmt').textContent = S.rupees(booking.foodCredit) + ' food credit';
        document.getElementById('restFc').textContent = S.rupees(booking.foodCredit) + ' food credit included';
        document.getElementById('foodCreditLine').textContent = CT.foodSection.creditLine;
      }
      // what your rate covers (wording depends on whether a food credit is set)
      document.getElementById('rateCovers').innerHTML =
        '<div class="rate-covers"><div class="rc-label">'+esc(CT.rateCovers.label)+'</div>'+
        '<p>'+esc(hasFood ? CT.rateCovers.withCredit : CT.rateCovers.withoutCredit)+'</p></div>';

      // deadline (absolute, computed from send time + hours); hide line if none
      document.getElementById('deadline').textContent = S.deadlineLabel(booking);

      renderCtas();
    }

    // ---- guest details + phone OTP, collected right here on the quote ------
    function renderGuestBlock(){
      var gb = document.getElementById('guestBlock');
      var g = booking.guest || {};
      if(g.phoneVerified){
        gb.innerHTML =
          '<div class="guest-row"><span>Name</span><strong>'+esc(g.name||'-')+'</strong></div>'+
          '<div class="guest-row"><span>Phone</span><span class="gval"><strong>'+esc(g.phone||g.whatsapp||'')+'</strong><span class="vbadge"> Verified</span></span></div>'+
          (g.email ? '<div class="guest-row"><span>Email</span><strong>'+esc(g.email)+'</strong></div>' : '');
        return;
      }
      gb.innerHTML =
        '<div class="gform">'+
          '<div id="gStep1">'+
            '<p class="gnote" style="margin-bottom:10px;">Add your details to confirm your stay.</p>'+
            '<div class="gfield"><span class="gfield-lbl">Full name</span><input type="text" id="gfName" placeholder="Your name" autocomplete="name"></div>'+
            '<div class="gfield" style="margin-top:10px;"><span class="gfield-lbl">Email</span><input type="email" id="gfEmail" placeholder="you@email.com" autocomplete="email"></div>'+
            '<div class="gfield" style="margin-top:10px;"><span class="gfield-lbl">Phone</span><div class="gphone"><span class="cc">+91</span><input type="tel" id="gfPhone" inputmode="numeric" maxlength="10" placeholder="98765 43210" autocomplete="tel-national"></div></div>'+
            '<div class="gerr" id="gfErr1" style="margin-top:8px;"></div>'+
            '<span class="btn primary" id="gfSend">Continue</span>'+
          '</div>'+
          '<div id="gStep2" hidden>'+
            '<p class="gfield-lbl">Security Check</p>'+
            '<p style="font-size:14px; margin-bottom:12px; line-height: 1.4;">Please verify you are human to proceed to payment.</p>'+
            '<div class="gfield" style="margin-top:10px; display:flex; justify-content:center; overflow:hidden;">'+
              '<div class="g-recaptcha" data-sitekey="6LfKp9MtAAAAADILeBlHphpcn7miDYH6Un0nu7rN"></div>'+
            '</div>'+
            '<div class="gerr" id="gfErr2" style="margin:8px 0;"></div>'+
            '<span class="btn primary" id="gfVerify">Verify & Continue</span>'+
            '<button type="button" class="glink" id="gfEdit" style="display:block;margin-top:12px;">&larr; Back to details</button>'+
          '</div>'+
        '</div>';
      wireGuestForm();
    }

    function wireGuestForm(){
      var d = function(s){ return String(s||'').replace(/\D/g,''); };
      var validEmail = function(s){ return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s); };
      var pretty = function(p){ return '+91 ' + p.slice(0,5) + ' ' + p.slice(5); };
      var g = function(id){ return document.getElementById(id); };
      var cur = { name:'', email:'', phone:'' };

      g('gfPhone').addEventListener('input', function(){ this.value = d(this.value).slice(0,10); });

      function step(n){ 
        g('gStep1').hidden = n!==1; 
        g('gStep2').hidden = n!==2; 
        if (n === 2 && window.grecaptcha && window.grecaptcha.render) {
            // Re-render explicitly if needed (usually auto-rendered by api.js)
            try { window.grecaptcha.reset(); } catch(e) {}
        }
      }
      
      function send(){
        var name = g('gfName').value.trim(), email = g('gfEmail').value.trim(), phone = d(g('gfPhone').value);
        if(name.length < 2){ g('gfErr1').textContent='Please enter your name.'; g('gfName').focus(); return; }
        if(!validEmail(email)){ g('gfErr1').textContent='Please enter a valid email.'; g('gfEmail').focus(); return; }
        if(phone.length !== 10){ g('gfErr1').textContent='Please enter a valid 10-digit number.'; g('gfPhone').focus(); return; }
        g('gfErr1').textContent='';
        
        cur = { name:name, email:email, phone:phone };
        step(2);
      }
      
      async function verify(){
        var token = window.grecaptcha ? grecaptcha.getResponse() : '';
        if (!token) {
          g('gfErr2').textContent = 'Please check the box to prove you are human.';
          return;
        }

        var btn = g('gfVerify');
        btn.textContent = 'Verifying...';
        btn.style.opacity = '0.7';
        btn.style.pointerEvents = 'none';
        
        try {
          var res = await fetch('/api/verify-recaptcha', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ token: token })
          });
          var data = await res.json();
          
          if (data.success) {
            booking = S.update(booking.id, { guest: { name: cur.name, email: cur.email, phone: pretty(cur.phone), whatsapp: pretty(cur.phone), phoneVerified: true } });
            renderGuestBlock();
            renderCtas();
          } else {
            g('gfErr2').textContent = 'Verification failed. Please try again.';
            if (window.grecaptcha) grecaptcha.reset();
            btn.textContent = 'Verify & Continue';
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
          }
        } catch(e) {
          console.error(e);
          g('gfErr2').textContent = 'Network error. Please try again.';
          if (window.grecaptcha) grecaptcha.reset();
          btn.textContent = 'Verify & Continue';
          btn.style.opacity = '1';
          btn.style.pointerEvents = 'auto';
        }
      }

      g('gfSend').addEventListener('click', send);
      g('gfVerify').addEventListener('click', verify);
      g('gfEdit').addEventListener('click', function(){ step(1); g('gfPhone').focus(); });

      g('gfName').addEventListener('keydown', function(e){ if(e.key==='Enter'){ e.preventDefault(); send(); } });
      g('gfEmail').addEventListener('keydown', function(e){ if(e.key==='Enter'){ e.preventDefault(); send(); } });
      g('gfPhone').addEventListener('keydown', function(e){ if(e.key==='Enter'){ e.preventDefault(); send(); } });
    }


    // nudge the guest up to the details form if they try to confirm unverified
    function flashGuestBlock(){
      var b = document.getElementById('guestBlock'); if(!b) return;
      b.classList.remove('flash'); void b.offsetWidth; b.classList.add('flash');
      b.scrollIntoView({ block:'center', behavior:'smooth' });
    }

    // ---- CTAs reflect status; clicking confirm/decline updates the store ----
    function renderCtas(){
      const st = S.effectiveStatus(booking);
      const cta = document.getElementById('ctaArea');
      const mobileBtn = document.getElementById('mobileConfirm');

      if(st === S.STATUS.CONFIRMED){
        var mealHref = waLink(CT.contact && CT.contact.whatsapp, "Hi, I'd like to pre-book meals for my confirmed Orchid Tree stay.");
        cta.innerHTML = '<div class="statusbanner confirmed"><span class="t">Confirmed</span>Thank you. Your stay is locked in. The resort team will be in touch.</div>'+
          '<a class="btn" href="'+esc(mealHref)+'" target="_blank" rel="noopener" style="text-decoration:none;">Pre-book your meals on WhatsApp</a>';
        mobileBtn.textContent = 'Confirmed'; mobileBtn.disabled = true;
      } else if(st === S.STATUS.DECLINED){
        cta.innerHTML = '<div class="statusbanner declined"><span class="t">Declined</span>You\'ve let us know this isn\'t right. Reach out any time to revisit.</div>';
        mobileBtn.textContent = 'Declined'; mobileBtn.disabled = true;
      } else if(st === S.STATUS.EXPIRED){
        cta.innerHTML = '<div class="statusbanner expired"><span class="t">This offer has expired</span>The confirmation window has passed. Please contact the resort for a fresh quote.</div>';
        mobileBtn.textContent = 'Expired'; mobileBtn.disabled = true;
      } else {
        var termsLink = CT.termsUrl
          ? '<a href="'+esc(CT.termsUrl)+'" target="_blank" rel="noopener">terms and conditions</a>'
          : '<a href="#" onclick="event.stopPropagation();event.preventDefault();openTerms();">terms and conditions</a>';
        var askHref = waLink(CT.contact && CT.contact.whatsapp, "Hi, I have a question about my Orchid Tree stay.");
        var verified = !!(booking.guest && booking.guest.phoneVerified);
        var verifyHint = verified ? '' :
          '<div class="verify-hint">Add and verify your details above to confirm your booking.</div>';
        cta.innerHTML =
          verifyHint +
          '<label class="tnc" id="tncLabel"><input type="checkbox" id="tncCheck">'+
            '<span>I have read and agree to the '+termsLink+'.</span></label>'+
          '<span class="btn primary disabled" id="confirmBtn">Agree to invoice &amp; confirm</span>'+
          '<a class="btn" href="'+esc(askHref)+'" target="_blank" rel="noopener" style="text-decoration:none;">Have a question? Message us</a>'+
          '<span class="btn link" id="declineBtn">Decline this offer</span>';
        var chk = document.getElementById('tncCheck');
        var cbtn = document.getElementById('confirmBtn');
        function syncTnc(){
          var ok = chk.checked && booking.guest && booking.guest.phoneVerified;
          cbtn.classList.toggle('disabled', !ok);
          mobileBtn.disabled = !ok;
        }
        function guardedConfirm(){
          if(!booking.guest || !booking.guest.phoneVerified){ flashGuestBlock(); return; }
          if(!chk.checked){ flashTnc(); return; }
          doConfirm();
        }
        chk.addEventListener('change', syncTnc);
        cbtn.addEventListener('click', guardedConfirm);
        document.getElementById('declineBtn').addEventListener('click', doDecline);
        mobileBtn.onclick = guardedConfirm;
        syncTnc();
      }
    }

    // nudge the guest to the terms checkbox if they try to confirm without it
    function flashTnc(){
      var l = document.getElementById('tncLabel'); if(!l) return;
      l.classList.remove('flash'); void l.offsetWidth; l.classList.add('flash');
      l.scrollIntoView({ block: 'center', behavior: 'smooth' });
    }

    async function doConfirm(){
      const btn = document.getElementById('confirmBtn');
      const mobileBtn = document.getElementById('mobileCbtn'); // there's also a mobile button
      
      if (btn) { btn.classList.add('busy'); btn.textContent = 'Confirming with Resort...'; }
      if (mobileBtn) { mobileBtn.disabled = true; mobileBtn.textContent = 'Confirming...'; }

      try {
        const res = await fetch('/api/create-booking', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            checkin: booking.stay.checkIn,
            checkout: booking.stay.checkOut,
            adults: booking.guestMix.adults,
            children: booking.guestMix.children,
            guestName: booking.guest.name,
            guestPhone: booking.guest.whatsapp || booking.guest.phone,
            guestEmail: booking.guest.email || "guest@orchidtree.in",
            roomIds: booking.roomIds,
            subtotal: booking.pricing.roomSubtotal
          })
        });

        const data = await res.json();
        if (data.status === true && data.bookingId) {
          booking.sfBookingId = data.bookingId;
          
          if (btn) btn.textContent = 'Generating Secure Checkout...';
          
          // Calculate total amount including taxes to charge guest
          const taxRate = 0.18;
          const taxes = Math.round(booking.pricing.roomSubtotal * taxRate);
          const totalAmount = booking.pricing.roomSubtotal + taxes;

          // Call our Vercel backend to create a Razorpay order
          const rzpRes = await fetch('/api/razorpay-order', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ amount: totalAmount })
          });
          const rzpData = await rzpRes.json();
          
          if (!rzpData.id) {
            alert("Failed to generate payment gateway order. Please try again.");
            if (btn) { btn.classList.remove('busy'); btn.textContent = 'Agree to invoice & confirm'; }
            if (mobileBtn) { mobileBtn.disabled = false; mobileBtn.textContent = 'Confirm booking'; }
            return;
          }

          var options = {
            "key": "rzp_live_ThKViVSs1B9jNs",
            "amount": rzpData.amount, // in paise
            "currency": "INR",
            "name": "Orchid Tree",
            "description": "Room Booking",
            "order_id": rzpData.id,
            "handler": async function (response) {
              if (btn) { btn.textContent = 'Securing Booking...'; btn.classList.add('busy'); }
              try {
                const confRes = await fetch('/api/confirm-payment', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({
                    bookingId: data.bookingId,
                    paymentId: response.razorpay_payment_id,
                    amount: totalAmount
                  })
                });
                const confData = await confRes.json();
                
                S.markConfirmed(booking.id);
                location.reload(); // Reload to show confirmed state
              } catch (e) {
                console.error('Payment confirmation error', e);
                alert("Payment received, but failed to confirm booking. Please contact the resort.");
              }
            },
            "prefill": {
              "name": booking.guest.name,
              "email": booking.guest.email || "guest@orchidtree.in",
              "contact": booking.guest.whatsapp || booking.guest.phone
            },
            "theme": { "color": "#2b3a2f" },
            "modal": {
              "ondismiss": function() {
                 if (btn) { btn.classList.remove('busy'); btn.textContent = 'Agree to invoice & confirm'; }
                 if (mobileBtn) { mobileBtn.disabled = false; mobileBtn.textContent = 'Confirm booking'; }
              }
            }
          };
          var rzp1 = new Razorpay(options);
          rzp1.open();
          return;
        } else {
          alert("Booking failed: " + (data.message || 'Unknown error'));
        }
      } catch (e) {
        console.error(e);
        alert("Network error. Please try again.");
      }

      if (btn) { btn.classList.remove('busy'); btn.textContent = 'Agree to invoice & confirm'; }
      if (mobileBtn) { mobileBtn.disabled = false; mobileBtn.textContent = 'Confirm booking'; }
    }
    function doDecline(){
      if(!confirm('Decline this offer? You can always contact the resort to revisit.')) return;
      booking = S.markDeclined(booking.id);
      renderCtas();
    }
    function openWhatsApp(){
      const num = (booking.guest.whatsapp||'').replace(/[^0-9]/g,'');
      const msg = encodeURIComponent('Hi, I\'d like to arrange meals for my Orchid Tree stay.');
      window.open('https://wa.me/'+num+'?text='+msg, '_blank');
    }

    // ---- carousel scroll affordance: arrows + edge fade --------------------
    function initCarousel(){
      var shorts = document.getElementById('incShorts');
      var nav = document.getElementById('incNav'), fade = document.getElementById('incFade');
      var prev = document.getElementById('incPrev'), next = document.getElementById('incNext');
      function stepPx(){ var t = shorts.querySelector('.tile'); return (t ? t.getBoundingClientRect().width : 262) + 18; }
      function sync(){
        var overflow = shorts.scrollWidth - shorts.clientWidth > 4;
        nav.style.display = overflow ? '' : 'none';
        fade.style.opacity = (overflow && shorts.scrollLeft < shorts.scrollWidth - shorts.clientWidth - 4) ? '1' : '0';
        prev.disabled = shorts.scrollLeft <= 2;
        next.disabled = shorts.scrollLeft >= shorts.scrollWidth - shorts.clientWidth - 2;
      }
      prev.onclick = function(){ shorts.scrollBy({ left: -stepPx() * 1.5, behavior: 'smooth' }); };
      next.onclick = function(){ shorts.scrollBy({ left: stepPx() * 1.5, behavior: 'smooth' }); };
      shorts.addEventListener('scroll', sync, { passive: true });
      window.addEventListener('resize', sync);
      sync();
    }

    // ---- static storytelling content (booking-independent) ----------------
    function renderContent(){
      // credibility band — highlighted pillars + a rating pillar with stars
      var c = CT.credibility;
      var pills = c.pillars.map(function(p){
        return '<div class="cred-item"><div class="cred-k">'+esc(p.k)+'</div><div class="cred-v">'+esc(p.v)+'</div></div>';
      });
      var rt = c.rating.text;
      var ratingLink = CT.googleReviewsUrl
        ? '<a href="'+esc(CT.googleReviewsUrl)+'" target="_blank" rel="noopener">'+esc(rt)+'</a>'
        : esc(rt);
      pills.push('<div class="cred-item">'+
        '<div class="cred-k"><span class="score">'+esc(c.rating.score)+'</span> <span class="stars">'+stars(c.rating.stars)+'</span></div>'+
        '<div class="cred-v">'+ratingLink+'</div></div>');
      document.getElementById('cred').innerHTML = pills.join('<div class="cred-sep"></div>');

      // wellness band + its review
      var w = CT.wellnessBand;
      document.getElementById('wellEyebrow').textContent = w.eyebrow;
      document.getElementById('wellTitle').textContent = w.title;
      document.getElementById('wellBody').textContent = w.body;
      if(w.cta){
        var wh = w.cta.whatsappUrl || waLink(CT.contact && CT.contact.whatsapp, "Hi, I'd like to add a massage to my Orchid Tree stay.");
        var wtgt = wh.charAt(0) === '#' ? '' : ' target="_blank" rel="noopener"';
        document.getElementById('wellCta').innerHTML = '<div class="meal-cta"><a href="'+esc(wh)+'"'+wtgt+'>'+esc(w.cta.label)+' &rarr;</a></div>';
      } else { document.getElementById('wellCta').innerHTML = ''; }
      applyImg('wellImg', w.imageUrl);
      document.getElementById('wellnessReview').innerHTML = reviewHtml(CT.reviewPlacements.wellness);

      // all-inclusive carousel
      var inc = CT.allInclusive;
      document.getElementById('incEyebrow').textContent = inc.eyebrow;
      document.getElementById('incTitle').textContent = inc.title;
      document.getElementById('incShorts').innerHTML = inc.items.map(function(it){
        // "More" is a link to a page chosen later; until moreUrl is set it
        // points to "#" and is styled as pending.
        var moreLink = it.moreUrl
          ? '<a class="more" href="'+esc(it.moreUrl)+'" target="_blank" rel="noopener">More &rarr;</a>'
          : ''; // no destination set yet — hide rather than dead-end at #
        return '<div class="tile">'+
          mediaHtml(it.imageUrl)+
          '<div class="scrim"></div>'+
          '<div class="hov"></div>'+
          '<div class="cap2">'+
            '<div class="lbl">'+esc(it.label)+'</div>'+
            '<div class="reveal">'+
              '<div class="desc">'+esc(it.short||'')+'</div>'+
              moreLink+
            '</div>'+
          '</div>'+
        '</div>';
      }).join('');

      // things to do (estate-wide, optional)
      var ex = CT.experiences;
      if(ex){
        document.getElementById('expEyebrow').textContent = ex.eyebrow;
        document.getElementById('expTitle').textContent = ex.title;
        document.getElementById('expNote').textContent = ex.note;
        document.getElementById('expGroups').innerHTML = (ex.groups || []).map(function(g){
          return '<div class="exp-group"><div class="exp-h">'+esc(g.label)+'</div><div class="exp-list">'+
            g.items.map(function(i){
              return '<div class="ei"><span class="ei-ic">'+iconSvg(i.icon)+'</span><span>'+esc(i.label)+'</span></div>';
            }).join('')+'</div></div>';
        }).join('');
      }

      // food section copy (the rupee ribbon is per-booking, set in render())
      var f = CT.foodSection;
      initCarousel();
      document.getElementById('foodEyebrow').textContent = f.eyebrow;
      document.getElementById('foodTitle').textContent = f.title;
      document.getElementById('foodBody').textContent = f.body;
      if(f.cta){
        var href = f.cta.whatsappUrl || waLink(CT.contact && CT.contact.whatsapp, "Hi, I'd like to pre-book meals for my Orchid Tree stay.");
        var tgt = href.charAt(0) === '#' ? '' : ' target="_blank" rel="noopener"';
        document.getElementById('mealCta').innerHTML =
          '<div class="meal-cta"><a href="'+esc(href)+'"'+tgt+'>'+esc(f.cta.label)+' &rarr;</a>'+
          (f.cta.note ? '<span class="note">'+esc(f.cta.note)+'</span>' : '')+'</div>';
      }
      applyImg('foodImg', f.imageUrl);
      document.getElementById('foodReview').innerHTML = reviewHtml(CT.reviewPlacements.food);

      // architect and estate band
      var a = CT.architectBand;
      document.getElementById('archEyebrow').textContent = a.eyebrow;
      document.getElementById('archTitle').textContent = a.title;
      document.getElementById('archBody').textContent = a.body;
      applyImg('archImg', a.imageUrl);

      // dedicated reviews band ("What guests say")
      document.getElementById('revTitle').textContent = CT.reviewsTitle || '';
      var secIds = (CT.reviewPlacements.section || []);
      document.getElementById('reviewsGrid').innerHTML = secIds.map(function(id){ return reviewHtml(id); }).filter(Boolean).join('');
      document.getElementById('reviewsAll').innerHTML = CT.googleReviewsUrl
        ? '<a class="review-all" href="'+esc(CT.googleReviewsUrl)+'" target="_blank" rel="noopener">Read all reviews on Google</a>'
        : '';

      // how your booking works (sourced logistics)
      document.getElementById('hwEyebrow').textContent = CT.howItWorks.eyebrow;
      document.getElementById('howworks').innerHTML = CT.howItWorks.steps.map(function(s, i){
        return '<div class="step"><span class="num">'+(i+1)+'</span><p>'+esc(s)+'</p></div>';
      }).join('');

      // where you will be (closing band) + policies
      document.getElementById('locEyebrow').textContent = CT.location.eyebrow;
      document.getElementById('locBody').textContent = CT.location.body;
      document.getElementById('policiesList').innerHTML = CT.policies.map(function(p){ return '<li>'+esc(p)+'</li>'; }).join('');
    }

    renderContent();
    render();
  })();
  
