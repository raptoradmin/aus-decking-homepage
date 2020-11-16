var spy_classes = '[class*=fade-]'

$(document).ready(function(){
	scrollspy()
	$('[lazy-src]').each(function(i,e){
		$(e).attr('src',$(e).attr('lazy-src'))
	})
	$('#CarHeader').fadeIn('slow')
})

$(window).scroll(function(){
	scrollspy()
	videospy()
	navspy()
})

var anime_nav = anime({
	targets: '#sect-nav',
	translateY: ['-100%', 0],
	delay: 1000,
	duration: 600,
	easing: 'easeOutCubic'
})

var anime_overlay = anime({
	targets: '.carousel-overlay *',
	translateX: ['-100vw', 0],
	delay: anime.stagger(120, {start: 800}),
	easing: 'spring(1, 80, 12, 1)'
})

var anime_summary = anime({
	targets: '#sect-summary .fade-rt',
	translateX: ['-100px', 0],
	opacity: 1,
	delay: anime.stagger(120),
	easing: 'spring(1, 80, 12, 1)',
	autoplay: false
})

var anime_metrics = anime({
	targets: '#sect-metrics .fade-up',
	top: 0,
	opacity: 1,
	delay: anime.stagger(120),
	autoplay: false
})

var anime_partners = anime({
	targets: '#sect-partners .fade-up',
	top: 0,
	opacity: 1,
	delay: function(el) { return el.offsetLeft/2 },
	autoplay: false
})

var anime_products = anime({
	targets: '#sect-products .fade-up',
	top: 0,
	opacity: 1,
	delay: function(el) { return el.offsetLeft/2 },
	autoplay: false
})

var anime_projects = anime({
	targets: '#sect-projects .fade-up',
	top: 0,
	opacity: 1,
	delay: anime.stagger(200, {grid: [2, 3]}),
	easing: 'easeOutCubic',
	autoplay: false
})

var anime_smbg = anime({
	targets: '#sect-smbg .fade-sd',
	opacity: 1,
	translateY: [50, 0],
	marginLeft: function(el,i) { return (i%2)?'auto':0 },
	marginRight: function(el,i) { return (i%2)?0:'auto' },
	delay: anime.stagger(120),
	easing: 'easeOutCubic',
	autoplay: true
})

var elems = [{
	tgt: '#sect-summary',
	anime: anime_summary
},{
	tgt: '#sect-metrics',
	anime: anime_metrics
},{
	tgt: '#sect-products .row',
	anime: anime_products
},{
	tgt: '#sect-partners .row',
	anime: anime_partners
},{
	tgt: '#sect-projects .row',
	anime: anime_projects
}]

function scrollspy() {
	elems.forEach(function(el){
		if($(el.tgt).position().top < $(window).scrollTop()+$(window).height()*0.8 && !el.anime.began) {
			el.anime.play()
		}
	})
}

function videospy() {
	tgt =  $('video').get(0)
	if($(tgt).position().top < $(window).scrollTop()) {
		tgt.play()
	}
}

function navspy() {
	if($(window).scrollTop() > 800) {
		$('#sect-nav').addClass('navbar-opaque')
	} else {
		$('#sect-nav').removeClass('navbar-opaque')
	}
}