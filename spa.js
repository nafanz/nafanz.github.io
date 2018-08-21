const PageType = {
	MainPageType: "main",
	SomePageType: "some",
	
	DefaultPageType: "main"
  };
  
  const mainPageTemplate = () => (`<div class="page"><span>main</span></div>`);
  const somePageTemplate = () => (`<div class="page"><span>some</span></div>`);
  
  const templates = {
	[ PageType.MainPageType ]: mainPageTemplate,
	[ PageType.SomePageType ]: somePageTemplate,
  }
  
  const router = {
	set( routeType ){
	  document.body.querySelector('main').innerHTML = templates[ routeType ]();
	}
  };
  
  router.set( PageType.DefaultPageType );
  
  // navigation
  
  document.body.querySelector('.button-group__navbar').addEventListener('click', ({target}) => {
	if( target.classList.contains( 'button-group__navbar__button' ) ){
	  router.set( target.dataset.route )
	}
  });