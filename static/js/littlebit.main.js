function mainOverlayDisable(){
  document.getElementById('overlayTop').classList.remove('main-open');
  document.getElementById('overlayTop').classList.add('main-close');
  document.getElementById('main-undertext').classList.remove('main-undertext-fadein');
  document.getElementById('main-undertext').classList.add('main-undertext-fadeout');
  document.getElementById('main-undertext').classList.remove('main-undertext-z')
  document.getElementById('overlayBottom').classList.remove('main-close', 'o-none');
  document.getElementById('overlayBottom').classList.add('main-open');
  document.getElementById('responsive-form').classList.remove('main-underlayout-fadeout');
  document.getElementById('responsive-form').classList.add('main-underlayout-fadein');
  document.getElementById('mainContainer').classList.remove('body-start-anim');
}

function mainOverlayEnable(){
  document.getElementById('overlayBottom').classList.remove('main-open');
  document.getElementById('overlayBottom').classList.add('main-close', 'o-none');
  document.getElementById('main-undertext').classList.remove('main-undertext-fadeout');
  document.getElementById('main-undertext').classList.add('main-undertext-fadein');
  document.getElementById('main-undertext').classList.add('main-undertext-z');
  document.getElementById('overlayTop').classList.remove('main-close');
  document.getElementById('overlayTop').classList.add('main-open');
  document.getElementById('responsive-form').classList.remove('main-underlayout-fadein');
  document.getElementById('responsive-form').classList.add('main-underlayout-fadeout');
  document.getElementById('mainContainer').classList.add('body-start-anim');
}
