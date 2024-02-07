/*function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}*/

function add_to_cart(elem) {
  document.cookie = elem.id + "=" + elem.value;
}



/* document.cookie='cart={"potato":1,"beetroot",2}'
var cart = JSON.parse(getCookie("cart"));
cart['onion']=20;
20
JSON.stringify(cart);
'{"potato":1,"beetroot":2,"onion":20}' */