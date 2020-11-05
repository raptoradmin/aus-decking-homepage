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
})

var anime_service = anime({
	targets: '#sect-service',
	translateY: ['40vh', 0],
	delay: 800,
	easing: 'spring(1, 80, 12, 1)'
})

var anime_partners = anime({
	targets: '#sect-partners .fade-up',
	top: 0,
	opacity: 1,
	delay: function(el) { return el.offsetLeft/2 },
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
	autoplay: false
})

var elems = [{
	tgt: '#sect-partners .fade-up',
	anime: anime_partners
},{
	tgt: '#sect-smbg .fade-sd',
	anime: anime_smbg
},{
	tgt: '#sect-service',
	anime: anime_service
}]

function scrollspy() {
	elems.forEach(function(el){
		if($(el.tgt).position().top < $(window).scrollTop()+$(window).height() && !el.anime.began) {
			el.anime.play()
		}
	})
}