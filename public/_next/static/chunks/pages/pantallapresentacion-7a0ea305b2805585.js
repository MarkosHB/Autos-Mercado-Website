(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[167],{5231:function(e,t,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/pantallapresentacion",function(){return r(5762)}])},2602:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var r in t)Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}(t,{default:function(){return i},noSSR:function(){return a}});let n=r(8754);r(5893),r(7294);let o=n._(r(5491));function s(e){return{default:(null==e?void 0:e.default)||e}}function a(e,t){return delete t.webpack,delete t.modules,e(t)}function i(e,t){let r=o.default,n={loading:e=>{let{error:t,isLoading:r,pastDelay:n}=e;return null}};e instanceof Promise?n.loader=()=>e:"function"==typeof e?n.loader=e:"object"==typeof e&&(n={...n,...e});let i=(n={...n,...t}).loader;return(n.loadableGenerated&&(n={...n,...n.loadableGenerated},delete n.loadableGenerated),"boolean"!=typeof n.ssr||n.ssr)?r({...n,loader:()=>null!=i?i().then(s):Promise.resolve(s(()=>null))}):(delete n.webpack,delete n.modules,a(r,n))}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},1159:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"LoadableContext",{enumerable:!0,get:function(){return n}});let n=r(8754)._(r(7294)).default.createContext(null)},5491:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return f}});let n=r(8754)._(r(7294)),o=r(1159),s=[],a=[],i=!1;function l(e){let t=e(),r={loading:!0,loaded:null,error:null};return r.promise=t.then(e=>(r.loading=!1,r.loaded=e,e)).catch(e=>{throw r.loading=!1,r.error=e,e}),r}class u{promise(){return this._res.promise}retry(){this._clearTimeouts(),this._res=this._loadFn(this._opts.loader),this._state={pastDelay:!1,timedOut:!1};let{_res:e,_opts:t}=this;e.loading&&("number"==typeof t.delay&&(0===t.delay?this._state.pastDelay=!0:this._delay=setTimeout(()=>{this._update({pastDelay:!0})},t.delay)),"number"==typeof t.timeout&&(this._timeout=setTimeout(()=>{this._update({timedOut:!0})},t.timeout))),this._res.promise.then(()=>{this._update({}),this._clearTimeouts()}).catch(e=>{this._update({}),this._clearTimeouts()}),this._update({})}_update(e){this._state={...this._state,error:this._res.error,loaded:this._res.loaded,loading:this._res.loading,...e},this._callbacks.forEach(e=>e())}_clearTimeouts(){clearTimeout(this._delay),clearTimeout(this._timeout)}getCurrentValue(){return this._state}subscribe(e){return this._callbacks.add(e),()=>{this._callbacks.delete(e)}}constructor(e,t){this._loadFn=e,this._opts=t,this._callbacks=new Set,this._delay=null,this._timeout=null,this.retry()}}function d(e){return function(e,t){let r=Object.assign({loader:null,loading:null,delay:200,timeout:null,webpack:null,modules:null},t),s=null;function l(){if(!s){let t=new u(e,r);s={getCurrentValue:t.getCurrentValue.bind(t),subscribe:t.subscribe.bind(t),retry:t.retry.bind(t),promise:t.promise.bind(t)}}return s.promise()}if(!i){let e=r.webpack?r.webpack():r.modules;e&&a.push(t=>{for(let r of e)if(t.includes(r))return l()})}function d(e,t){!function(){l();let e=n.default.useContext(o.LoadableContext);e&&Array.isArray(r.modules)&&r.modules.forEach(t=>{e(t)})}();let a=n.default.useSyncExternalStore(s.subscribe,s.getCurrentValue,s.getCurrentValue);return n.default.useImperativeHandle(t,()=>({retry:s.retry}),[]),n.default.useMemo(()=>{var t;return a.loading||a.error?n.default.createElement(r.loading,{isLoading:a.loading,pastDelay:a.pastDelay,timedOut:a.timedOut,error:a.error,retry:s.retry}):a.loaded?n.default.createElement((t=a.loaded)&&t.default?t.default:t,e):null},[e,a])}return d.preload=()=>l(),d.displayName="LoadableComponent",n.default.forwardRef(d)}(l,e)}function c(e,t){let r=[];for(;e.length;){let n=e.pop();r.push(n(t))}return Promise.all(r).then(()=>{if(e.length)return c(e,t)})}d.preloadAll=()=>new Promise((e,t)=>{c(s).then(e,t)}),d.preloadReady=e=>(void 0===e&&(e=[]),new Promise(t=>{let r=()=>(i=!0,t());c(a,e).then(r,r)})),window.__NEXT_PRELOADREADY=d.preloadReady;let f=d},5762:function(e,t,r){"use strict";r.r(t),r.d(t,{Div_602c14884fa2de27f522fe8f94374b02:function(){return E},Errorboundary_8e2846cc6efed882697577dedf963bd6:function(){return w},Fragment_f2f0916d2fcc08b7cdf76cec697f0750:function(){return k},Img_2e3727c65ddb7f05dd11203d6233595f:function(){return H},Moment_d7fba2cf42b1edbcc4585a544acd680c:function(){return V},Toaster_6e6ebf8d7ce589d59b7d382fb7576edf:function(){return j},default:function(){return Z}});var n=r(2729),o=r(5944),s=r(4511),a=r(7294),i=r(8039),l=r(9654),u=r(917),d=r(2658),c=r(4712),f=r(3954),_=r(4390),h=r(4298),p=r.n(h),m=r(5152),g=r.n(m),b=r(9008),x=r.n(b);function y(){let e=(0,n._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return y=function(){return e},e}let v=g()(()=>Promise.all([r.e(885),r.e(803)]).then(r.t.bind(r,4803,23)),{loadableGenerated:{webpack:()=>[4803]},ssr:!1}),C=(0,u.keyframes)(y());function w(){let[e,t]=(0,a.useContext)(i.EventLoopContext),r=(0,a.useCallback)((t,r)=>e([(0,l.Event)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:t.stack,component_stack:r.componentStack},{})],[t,r],{}),[e,l.Event]);return(0,o.BX)(s.SV,{fallbackRender:t=>(0,u.jsx)("div",{css:{height:"100%",width:"100%",position:"absolute",display:"flex",alignItems:"center",justifyContent:"center"}},(0,u.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem"}},(0,u.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem",maxWidth:"50ch",border:"1px solid #888888",borderRadius:"0.25rem",padding:"1rem"}},(0,u.jsx)("h2",{css:{fontSize:"1.25rem",fontWeight:"bold"}},(0,u.jsx)(a.Fragment,{},"An error occurred while rendering this page.")),(0,u.jsx)("p",{css:{opacity:"0.75"}},(0,u.jsx)(a.Fragment,{},"This is an error with the application itself.")),(0,u.jsx)("details",{},(0,u.jsx)("summary",{css:{padding:"0.5rem"}},(0,u.jsx)(a.Fragment,{},"Error message")),(0,u.jsx)("div",{css:{width:"100%",maxHeight:"50vh",overflow:"auto",background:"#000",color:"#fff",borderRadius:"0.25rem"}},(0,u.jsx)("div",{css:{padding:"0.5rem",width:"fit-content"}},(0,u.jsx)("pre",{},(0,u.jsx)(a.Fragment,{},t.error.stack)))),(0,u.jsx)("button",{css:{padding:"0.35rem 0.75rem",margin:"0.5rem",background:"#fff",color:"#000",border:"1px solid #000",borderRadius:"0.25rem",fontWeight:"bold"},onClick:function(){for(var r=arguments.length,n=Array(r),o=0;o<r;o++)n[o]=arguments[o];return e([(0,l.Event)("_call_function",{function:()=>navigator.clipboard.writeText(t.error.stack)},{})],n,{})}},(0,u.jsx)(a.Fragment,{},"Copy")))),(0,u.jsx)("hr",{css:{borderColor:"currentColor",opacity:"0.25"}}),(0,u.jsx)("a",{href:"https://reflex.dev"},(0,u.jsx)("div",{css:{display:"flex",alignItems:"baseline",justifyContent:"center",fontFamily:"monospace","--default-font-family":"monospace",gap:"0.5rem"}},(0,u.jsx)(a.Fragment,{},"Built with "),(0,u.jsx)("svg",{css:{viewBox:"0 0 56 12",fill:"currentColor"},height:"12",width:"56",xmlns:"http://www.w3.org/2000/svg"},(0,u.jsx)("path",{d:"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}),(0,u.jsx)("path",{d:"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}),(0,u.jsx)("path",{d:"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}),(0,u.jsx)("path",{d:"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}),(0,u.jsx)("path",{d:"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}),(0,u.jsx)("path",{d:"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"})))))),onError:r,children:[(0,o.BX)(a.Fragment,{children:[(0,o.tZ)(E,{}),(0,o.tZ)(j,{})]}),(0,o.BX)(_.Box,{css:{width:"100vw",height:"100vh"},children:[(0,o.tZ)(p(),{strategy:"afterInteractive",children:"document.documentElement.lang='es'"}),(0,o.tZ)(_.Flex,{css:{display:"flex",alignItems:"center",justifyContent:"center",width:"100vw",height:"100vh"},children:(0,o.BX)(_.Flex,{align:"start",className:"rx-Stack",css:{width:"100vw",height:"100vh"},direction:"column",gap:"3",children:[(0,o.tZ)(H,{}),(0,o.tZ)(V,{})]})})]}),(0,o.BX)(x(),{children:[(0,o.tZ)("title",{children:"Autosmercado | Pantallapresentacion"}),(0,o.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}function V(){let e=(0,a.useContext)(i.StateContexts.reflex___state____state__autosmercado___supabase____presentation_state____presentation_state),[t,r]=(0,a.useContext)(i.EventLoopContext),n=(0,a.useCallback)(e=>t([(0,l.Event)("reflex___state____state.autosmercado___supabase____presentation_state____presentation_state.cambiar_imagen",{},{})],[e],{}),[t,l.Event]);return(0,o.tZ)(v,{css:{display:"none"},format:"HH:mm:ss",interval:e.interval,onChange:n})}function j(){let{resolvedColorMode:e}=(0,a.useContext)(i.ColorModeContext);l.refs.__toast=c.Am;let[t,r]=(0,a.useContext)(i.EventLoopContext),n={description:"Check if server is reachable at "+(0,l.getBackendURL)(f.Ks).href,closeButton:!0,duration:12e4,id:"websocket-error"},[s,u]=(0,a.useState)(!1);return(0,a.useEffect)(()=>{r.length>=2?s||c.Am.error("Cannot connect to server: ".concat(r.length>0?r[r.length-1].message:"","."),{...n,onDismiss:()=>u(!0)}):(c.Am.dismiss("websocket-error"),u(!1))},[r]),(0,o.tZ)(c.x7,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function H(){let e=(0,a.useContext)(i.StateContexts.reflex___state____state__autosmercado___supabase____presentation_state____presentation_state);return(0,o.tZ)("img",{css:{width:"100%",height:"100%",objectFit:"contain"},src:e.fotos_presentacion.at(e.current_image_idx)})}function E(){let[e,t]=(0,a.useContext)(i.EventLoopContext);return(0,o.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: "+(t.length>0?t[t.length-1].message:""),children:(0,o.tZ)(k,{})})}function k(){let[e,t]=(0,a.useContext)(i.EventLoopContext);return(0,o.tZ)(a.Fragment,{children:(0,l.isTrue)(t.length>0)?(0,o.tZ)(a.Fragment,{children:(0,o.tZ)(d.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:C+" 1s infinite"},size:32})}):(0,o.tZ)(a.Fragment,{})})}function Z(){return(0,o.tZ)(w,{})}},5152:function(e,t,r){e.exports=r(2602)},4298:function(e,t,r){e.exports=r(3381)},4511:function(e,t,r){"use strict";r.d(t,{SV:function(){return a}});var n=r(7294);let o=(0,n.createContext)(null),s={didCatch:!1,error:null};class a extends n.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=s}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var t,r,n=arguments.length,o=Array(n),a=0;a<n;a++)o[a]=arguments[a];null===(t=(r=this.props).onReset)||void 0===t||t.call(r,{args:o,reason:"imperative-api"}),this.setState(s)}}componentDidCatch(e,t){var r,n;null===(r=(n=this.props).onError)||void 0===r||r.call(n,e,t)}componentDidUpdate(e,t){let{didCatch:r}=this.state,{resetKeys:n}=this.props;if(r&&null!==t.error&&function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==t.length||e.some((e,r)=>!Object.is(e,t[r]))}(e.resetKeys,n)){var o,a;null===(o=(a=this.props).onReset)||void 0===o||o.call(a,{next:n,prev:e.resetKeys,reason:"keys"}),this.setState(s)}}render(){let{children:e,fallbackRender:t,FallbackComponent:r,fallback:s}=this.props,{didCatch:a,error:i}=this.state,l=e;if(a){let e={error:i,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof t)l=t(e);else if(r)l=(0,n.createElement)(r,e);else if(void 0!==s)l=s;else throw i}return(0,n.createElement)(o.Provider,{value:{didCatch:a,error:i,resetErrorBoundary:this.resetErrorBoundary}},l)}}}},function(e){e.O(0,[49,888,774,179],function(){return e(e.s=5231)}),_N_E=e.O()}]);