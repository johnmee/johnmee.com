(function(c,a){window.mixpanel=a;var b,d,h,e;b=c.createElement("script");
b.type="text/javascript";b.async=!0;b.src=("https:"===c.location.protocol?"https:":"http:")+
'//cdn.mxpnl.com/libs/mixpanel-2.2.min.js';d=c.getElementsByTagName("script")[0];
d.parentNode.insertBefore(b,d);a._i=[];a.init=function(b,c,f){function d(a,b){
var c=b.split(".");2==c.length&&(a=a[c[0]],b=c[1]);a[b]=function(){a.push([b].concat(
Array.prototype.slice.call(arguments,0)))}}var g=a;"undefined"!==typeof f?g=a[f]=[]:
f="mixpanel";g.people=g.people||[];h=['disable','track','track_pageview','track_links',
'track_forms','register','register_once','unregister','identify','alias','name_tag','set_config',
'people.set','people.set_once','people.increment','people.track_charge','people.append'];
for(e=0;e<h.length;e++)d(g,h[e]);a._i.push([b,c,f])};a.__SV=1.2;})(document,window.mixpanel||[]);
mixpanel.init("a93c9738f3fd0a687e5c26149c8417af");
mixpanel.track("Home");
mixpanel.track_links('a','clicked link');