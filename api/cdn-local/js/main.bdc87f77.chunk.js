(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{27:function(e,a,t){e.exports=t(44)},32:function(e,a,t){},39:function(e,a,t){},42:function(e,a,t){},43:function(e,a,t){},44:function(e,a,t){"use strict";t.r(a);var n=t(0),c=t.n(n),l=t(22),s=t.n(l),r=(t(32),t(10)),i=t(11);var o=function(){return c.a.createElement("div",{className:"container"},c.a.createElement("div",{className:"container",id:"navbar-container"},c.a.createElement("nav",{className:"navbar is-fixed-top"},c.a.createElement("div",{className:"navbar-brand"},c.a.createElement("h3",{className:"navbar-item"})),c.a.createElement("div",{className:"navbar-start"},c.a.createElement(r.b,{to:"/new/blog",className:"navbar-item",style:{textDecoration:"none"}},c.a.createElement("a",{className:"navbar-item"},"New Post")),c.a.createElement(r.b,{to:"/products",className:"navbar-item",style:{textDecoration:"none"}},c.a.createElement("a",{className:"navbar-item"},"Products")),c.a.createElement(r.b,{to:"/items",className:"navbar-item",style:{textDecoration:"none"}},c.a.createElement("a",{className:"navbar-item"},"Items")),"          "),c.a.createElement("div",{className:"navbar-end"},c.a.createElement("a",{className:"navbar-item"},c.a.createElement("i",{className:"far fa-envelope"})),c.a.createElement("a",{className:"navbar-item"},c.a.createElement("i",{className:"fab fa-facebook"})),c.a.createElement("a",{className:"navbar-item"},c.a.createElement("i",{className:"fab fa-instagram"})),c.a.createElement("a",{className:"navbar-item"},c.a.createElement("i",{className:"fab fa-youtube"})),c.a.createElement("a",{className:"navbar-item"},c.a.createElement("i",{className:"fab fa-pinterest"})),c.a.createElement("a",{className:"navbar-item"})))))};var m=function(){return c.a.createElement("footer",{className:"footer has-text-centered is-fixed-bottom"},c.a.createElement("div",{className:"content"},"footer"))};var u=function(){return c.a.createElement("section",{className:"hero"},c.a.createElement("div",{className:"hero-body"},c.a.createElement("div",{className:"has-text-centered"},c.a.createElement("h1",{className:"title custom-font "},"Unorthodox Mom"),c.a.createElement("h2",{className:"subtitle custom-font"},"Subtitle"))))};var d=function(){return c.a.createElement("aside",{className:"about card column is-2 is-shadowless"},c.a.createElement("div",{className:"card-content"},c.a.createElement("div",{className:""},c.a.createElement("figure",{class:"card-image is-4by3 "},c.a.createElement("img",{class:"",src:"https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1534&q=80"})),c.a.createElement("h1",{className:"has-text-centered subtitle custom-font"},"About")),c.a.createElement("div",{className:""},"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fusce id velit ut tortor pretium viverra suspendisse. Scelerisque eleifend donec pretium vulputate sapien nec. Amet justo donec enim diam vulputate ut pharetra. Augue lacus viverra vitae congue eu consequat ac. At lectus urna duis convallis."),c.a.createElement("div",{className:""})))},p=t(5),E=t(6),h=t(8),v=t(7),b=t(9),f=t(15),g=t.n(f),N=(t(39),function(e){function a(e){var t;return Object(p.a)(this,a),(t=Object(h.a)(this,Object(v.a)(a).call(this,e))).state={posts:[],isLoaded:!1},t}return Object(b.a)(a,e),Object(E.a)(a,[{key:"componentDidMount",value:function(){var e=this;fetch("/api/v1/blog_post/").then(function(e){return e.json()}).then(function(a){e.setState({isLoaded:!0,posts:a})})}},{key:"render",value:function(){var e=this.state,a=e.isLoaded,t=e.posts;return a?c.a.createElement("div",{id:"posts",class:"clearfix"},t.map(function(e){return c.a.createElement("figure",{class:"post card"},c.a.createElement("div",{class:"card-image"},c.a.createElement("div",{class:"image is-3by2"},c.a.createElement("img",{class:"",src:e.images}))),c.a.createElement("figcaption",{class:"card-body"},c.a.createElement("h2",null,e.title),e.post.length>50?c.a.createElement("div",null,"".concat(e.post.substring(0,50),"...")):c.a.createElement("p",null,e.post)),c.a.createElement(r.b,{to:"/blog/".concat(e.slug),title:"Read more"},"Read more"))})):c.a.createElement("div",null,"Loading...")}}]),a}(n.Component));var y=function(){return c.a.createElement("div",null,c.a.createElement(u,null),c.a.createElement(d,null),c.a.createElement(N,null))},j=t(25),O=t(14),x=t(26),k=t.n(x),w=function(e){function a(e){var t;return Object(p.a)(this,a),(t=Object(h.a)(this,Object(v.a)(a).call(this,e))).handleSubmit=t.handleSubmit.bind(Object(O.a)(t)),t.handleInputChange=t.handleInputChange.bind(Object(O.a)(t)),t.state={title:"",post:"",tags:"",images:null,video_link:""},t}return Object(b.a)(a,e),Object(E.a)(a,[{key:"handleSubmit",value:function(e){e.preventDefault();var a=this.state;this.submitPost(a)}},{key:"submitPost",value:function(e){var a=k.a.load("csrftoken"),t=new FormData;t.append("images",e.image),t.append("post",e.post),t.append("title",e.title),t.append("tags",e.tags),fetch("/api/v1/blog_post/",{method:"POST",headers:{Accept:"application/json","X-CSRFToken":a},body:t}).then(function(e){return e.json()}).then(function(e){console.log(e)}).catch(function(e){console.log("error",e)})}},{key:"handleInputChange",value:function(e){e.preventDefault(),this.setState(Object(j.a)({},e.target.name,e.target.value))}},{key:"render",value:function(){return c.a.createElement("div",null,c.a.createElement("form",{onSubmit:this.handleSubmit},c.a.createElement("input",{type:"text",placeholder:"Title",name:"title",className:"input",onChange:this.handleInputChange,required:"reaquired"}),c.a.createElement("textarea",{type:"textarea",name:"post",className:"textarea",onChange:this.handleInputChange,required:"reaquired"}),c.a.createElement("div",{class:"file has-name is-right"},c.a.createElement("label",{class:"file-label"},c.a.createElement("input",{class:"file-input",name:"images",type:"file",onChange:this.handleInputChange}),c.a.createElement("span",{class:"file-cta"},c.a.createElement("span",{class:"file-icon"},c.a.createElement("i",{class:"fas fa-upload"})),c.a.createElement("span",{class:"file-label"},"Choose a file\u2026")),c.a.createElement("span",{class:"file-name"}))),c.a.createElement("input",{type:"text",placeholder:"tags",name:"tags",className:"input",onChange:this.handleInputChange}),c.a.createElement("input",{type:"submit",value:"Submit",name:"submit",className:"button"})))}}]),a}(n.Component),C=function(e){function a(e){var t;return Object(p.a)(this,a),(t=Object(h.a)(this,Object(v.a)(a).call(this,e))).state={comments:[],isLoaded:!1},console.log(e),t}return Object(b.a)(a,e),Object(E.a)(a,[{key:"componentDidMount",value:function(){var e=this;fetch("http://localhost:8000/api/v1/comments/?blog_post=".concat(this.props.id)).then(function(e){return e.json()}).then(function(a){e.setState({isLoaded:!0,comments:a})})}},{key:"render",value:function(){var e=this.state,a=e.isLoaded,t=e.comments;return a?c.a.createElement("section",{className:"section"},t.map(function(e){return c.a.createElement("article",{class:"media comments-box"},c.a.createElement("div",{class:"media-content"},c.a.createElement("div",{class:"content"},c.a.createElement("p",null,c.a.createElement("strong",null,e.name),c.a.createElement("br",null),e.comment_body)),c.a.createElement("nav",{class:"level is-mobile"},c.a.createElement("div",{class:"level-left"}))))})):c.a.createElement("div",null,"Loading...")}}]),a}(n.Component),S=(t(42),function(e){function a(e){var t;return Object(p.a)(this,a),(t=Object(h.a)(this,Object(v.a)(a).call(this,e))).state={post:[],isLoaded:!1,postid:e.match},t}return Object(b.a)(a,e),Object(E.a)(a,[{key:"componentDidMount",value:function(){var e=this;fetch("/api/v1/blog_post/".concat(this.props.match.params.slug)).then(function(e){return e.json()}).then(function(a){e.setState({isLoaded:!0,post:a})})}},{key:"render",value:function(){var e=this.state,a=e.isLoaded,t=e.post;e.postid;return a?c.a.createElement("div",{className:"section"},c.a.createElement(d,null),c.a.createElement("div",{className:"container"},c.a.createElement("div",{className:"post-body"},c.a.createElement("h1",{className:"custom-font"},t.title),c.a.createElement("p",null,c.a.createElement("strong",null,c.a.createElement("em",null,c.a.createElement(g.a,{format:"YYYY/MM/DD"},t.created)," ")," by Writerton McWriterpants")),c.a.createElement("p",null,c.a.createElement("img",{className:"",src:t.images})),c.a.createElement("p",{className:""},t.post),c.a.createElement(C,{id:t.id}),c.a.createElement("div",{className:"tag"},t.tags)))):c.a.createElement("div",null,"Loading...")}}]),a}(n.Component));t(43);var L=function(){return c.a.createElement(r.a,null,c.a.createElement("div",{className:"App"},c.a.createElement("header",{className:"App-header"}),c.a.createElement(o,null),c.a.createElement(i.c,null,c.a.createElement("section",{className:"main-content"},c.a.createElement(i.a,{path:"/",exact:!0,component:y}),c.a.createElement(i.a,{path:"/new/blog",exact:!0,component:w}),c.a.createElement(i.a,{path:"/blog/:slug",component:S}))),c.a.createElement(m,null)))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));s.a.render(c.a.createElement(L,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[27,1,2]]]);
//# sourceMappingURL=main.bdc87f77.chunk.js.map