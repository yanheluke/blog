let scrollPos=0, currentSection='writing';
let currentAlbum=null, currentPhotoIdx=0;
let savedHeroStyle=null, savedHeroInner=null;

// ── Theme ──
function toggleTheme(){
  var html=document.documentElement;
  var current=html.getAttribute('data-theme');
  var next=current==='dark'?'light':'dark';
  html.setAttribute('data-theme',next);
  localStorage.setItem('theme',next);
}
function initTheme(){
  var saved=localStorage.getItem('theme');
  if(saved){document.documentElement.setAttribute('data-theme',saved);}
  else if(window.matchMedia('(prefers-color-scheme:light)').matches){document.documentElement.setAttribute('data-theme','light');}
}
window.matchMedia('(prefers-color-scheme:dark)').addEventListener('change',function(e){
  if(!localStorage.getItem('theme')){document.documentElement.setAttribute('data-theme',e.matches?'dark':'light');}
});

function accentTitle(t){
  var m=t.match(/^(.+?)([，。：:｜|\s\-—–].*)$/);
  if(m)return '<em>'+m[1]+'</em>'+m[2];
  if(/[一-鿿]/.test(t.charAt(0)))return '<em>'+t.substring(0,2)+'</em>'+t.substring(2);
  var sp=t.indexOf(' ');if(sp>0)return '<em>'+t.substring(0,sp)+'</em>'+t.substring(sp);
  return '<em>'+t+'</em>';
}

function heroEl(){return document.getElementById('hero-writing');}
function acadEl(){return document.getElementById('hero-academic');}
function galEl(){return document.getElementById('hero-gallery');}
function abtEl(){return document.getElementById('hero-about');}

function showSectionHero(s){
  var w=heroEl(), a=acadEl(), g=galEl(), ab=abtEl();
  if(w)w.style.display='none';if(a)a.style.display='none';if(g)g.style.display='none';if(ab)ab.style.display='none';
  if(s==='writing'){if(w)w.style.display='block';}
  else if(s==='academic'){if(a)a.style.display='block';}
  else if(s==='gallery'){if(g)g.style.display='block';}
  else if(s==='about'){if(ab)ab.style.display='block';}
}

function switchSection(s){
  if(currentSection===s)return;
  currentSection=s;scrollPos=0;
  closeArticle(true);
  showGalleryList(); // Reset gallery to album list view
  document.querySelectorAll('.sidebar-item').forEach(function(i){i.classList.remove('active')});
  document.getElementById('nav-'+s).classList.add('active');
  document.querySelectorAll('.section-content').forEach(function(c){c.classList.remove('active')});
  var sc=document.getElementById('section-'+s);
  if(sc)sc.classList.add('active');
  showSectionHero(s);
  window.scrollTo({top:0,behavior:'instant'});
}

// ── Gallery ──
function openAlbum(id){
  document.getElementById('gallery-list').style.display='none';
  document.querySelectorAll('.gallery-album').forEach(function(a){a.style.display='none'});
  var el=document.getElementById(id);if(el)el.style.display='block';
  currentAlbum=id;
  window.scrollTo({top:0,behavior:'instant'});
}
function showGalleryList(){
  document.getElementById('gallery-list').style.display='grid';
  document.querySelectorAll('.gallery-album').forEach(function(a){a.style.display='none'});
  currentAlbum=null;
}

// ── Lightbox ──
function openLightbox(idx){
  if(!currentAlbum||!lightboxData||!lightboxData[currentAlbum])return;
  currentPhotoIdx=idx;
  var lb=document.getElementById('lightbox');
  var img=document.getElementById('lightbox-img');
  var counter=document.getElementById('lightbox-counter');
  var photos=lightboxData[currentAlbum];
  img.src=photos[idx];
  counter.textContent=(idx+1)+' / '+photos.length;
  lb.classList.add('active');
  document.body.style.overflow='hidden';
}
function closeLightbox(){
  document.getElementById('lightbox').classList.remove('active');
  document.body.style.overflow='';
}
function navLightbox(dir){
  if(!currentAlbum||!lightboxData||!lightboxData[currentAlbum])return;
  var photos=lightboxData[currentAlbum];
  currentPhotoIdx=(currentPhotoIdx+dir+photos.length)%photos.length;
  document.getElementById('lightbox-img').src=photos[currentPhotoIdx];
  document.getElementById('lightbox-counter').textContent=(currentPhotoIdx+1)+' / '+photos.length;
}
document.addEventListener('keydown',function(e){
  if(document.getElementById('lightbox').classList.contains('active')){
    if(e.key==='Escape')closeLightbox();
    else if(e.key==='ArrowLeft')navLightbox(-1);
    else if(e.key==='ArrowRight')navLightbox(1);
  }else if(e.key==='Escape'){closeArticle();showGalleryList();}
});

// ── Articles ──
function openArticle(id){
  scrollPos=window.scrollY;
  document.querySelectorAll('.section-content').forEach(function(c){c.style.display='none'});
  document.querySelectorAll('.article-page').forEach(function(p){p.classList.remove('active')});
  var el=document.getElementById(id);if(el)el.classList.add('active');
  var cover=el.getAttribute('data-cover');
  var title=el.querySelector('header h1');
  var titleText=title?title.textContent:'';
  var dateEl=el.querySelector('header time');
  var dateText=dateEl?dateEl.textContent:'';
  var subText=el.getAttribute('data-subtitle')||'';
  if(cover||titleText){
    var h=heroEl();if(!h||h.style.display==='none')h=acadEl();
    if(h){
      if(savedHeroStyle===null)savedHeroStyle=h.getAttribute('style');
      if(savedHeroInner===null)savedHeroInner=h.querySelector('.hero-inner').innerHTML;
      if(cover){
        h.setAttribute('style',h.getAttribute('style')+';background-image:linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.45)),url('+cover+');background-size:cover;background-position:center');
      }
      if(titleText){
        var heroHTML='<h1 class="article-title">'+accentTitle(titleText)+'</h1>';
        if(subText)heroHTML+='<p class="article-subtitle">'+subText+'</p>';
        if(dateText)heroHTML+='<div class="article-meta">'+dateText+'</div>';
        h.querySelector('.hero-inner').innerHTML=heroHTML;
        h.classList.add('article-view');
      }
    }
  }
  window.scrollTo({top:0,behavior:'instant'});
  history.pushState({article:id,section:currentSection},'','#'+id);
}

function closeArticle(silent){
  document.querySelectorAll('.section-content').forEach(function(c){c.style.display='';});
  document.querySelectorAll('.article-page').forEach(function(p){p.classList.remove('active')});
  if(savedHeroStyle!==null){
    var h=heroEl();if(!h||h.style.display==='none')h=acadEl();
    if(h){
      h.setAttribute('style',savedHeroStyle);
      h.classList.remove('article-view');
    }
    savedHeroStyle=null;
  }
  if(savedHeroInner!==null){
    var h2=heroEl();if(!h2||h2.style.display==='none')h2=acadEl();
    if(h2)h2.querySelector('.hero-inner').innerHTML=savedHeroInner;
    savedHeroInner=null;
  }
  showSectionHero(currentSection);
  if(!silent)history.pushState({section:currentSection},'',window.location.pathname);
  requestAnimationFrame(function(){window.scrollTo({top:scrollPos,behavior:'instant'});});
}

window.addEventListener('popstate',function(e){
  if(e.state&&e.state.article){
    if(e.state.section&&e.state.section!==currentSection){
      currentSection=e.state.section;
      document.querySelectorAll('.sidebar-item').forEach(function(i){i.classList.remove('active')});
      document.getElementById('nav-'+currentSection).classList.add('active');
      document.querySelectorAll('.section-content').forEach(function(c){c.classList.remove('active')});
      var sc=document.getElementById('section-'+currentSection);
      if(sc)sc.classList.add('active');
      showSectionHero(currentSection);
    }
    document.querySelectorAll('.section-content').forEach(function(c){c.style.display='none'});
    document.querySelectorAll('.article-page').forEach(function(p){p.classList.remove('active')});
    var el=document.getElementById(e.state.article);if(el)el.classList.add('active');
    var cover=el.getAttribute('data-cover');
    var title=el.querySelector('header h1');
    var titleText=title?title.textContent:'';
    var dateEl=el.querySelector('header time');
    var dateText=dateEl?dateEl.textContent:'';
    var subText=el.getAttribute('data-subtitle')||'';
    if(cover||titleText){
      var h=heroEl();if(!h||h.style.display==='none')h=acadEl();
      if(h){
        if(savedHeroStyle===null)savedHeroStyle=h.getAttribute('style');
        if(savedHeroInner===null)savedHeroInner=h.querySelector('.hero-inner').innerHTML;
        if(cover){
          h.setAttribute('style',h.getAttribute('style')+';background-image:linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.45)),url('+cover+');background-size:cover;background-position:center');
        }
        if(titleText){
          var heroHTML2='<h1 class="article-title">'+accentTitle(titleText)+'</h1>';
          if(subText)heroHTML2+='<p class="article-subtitle">'+subText+'</p>';
          if(dateText)heroHTML2+='<div class="article-meta">'+dateText+'</div>';
          h.querySelector('.hero-inner').innerHTML=heroHTML2;
          h.classList.add('article-view');
        }
      }
    }
    window.scrollTo({top:0,behavior:'instant'});
  }else{
    if(savedHeroStyle!==null){
      var h=heroEl();if(!h||h.style.display==='none')h=acadEl();
      if(h){
        h.setAttribute('style',savedHeroStyle);
        h.classList.remove('article-view');
      }
      savedHeroStyle=null;
    }
    if(savedHeroInner!==null){
      var h2=heroEl();if(!h2||h2.style.display==='none')h2=acadEl();
      if(h2)h2.querySelector('.hero-inner').innerHTML=savedHeroInner;
      savedHeroInner=null;
    }
    closeArticle(true);showGalleryList();
  }
});

// ── Topbar scroll reveal ──
window.addEventListener('scroll',function(){
  var heroes=document.querySelectorAll('.hero.has-bg'),hero=null;
  for(var i=0;i<heroes.length;i++){if(heroes[i].offsetHeight>0){hero=heroes[i];break;}}
  var threshold=hero?hero.offsetHeight-56:300;
  document.querySelector('.topbar').classList.toggle('scrolled',window.scrollY>threshold);
},{passive:true});

document.addEventListener('DOMContentLoaded',function(){
  initTheme();
  showSectionHero('writing');
  var h=window.location.hash.slice(1);
  if(h&&document.getElementById(h))openArticle(h);
});
