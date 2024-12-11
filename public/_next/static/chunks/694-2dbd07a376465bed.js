"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[694],{2171:function(e,t,n){n.d(t,{Z:function(){return r}});let r=(0,n(6583).Z)("ChevronDown",[["path",{d:"m6 9 6 6 6-6",key:"qrunsl"}]])},4598:function(e,t,n){n.d(t,{Z:function(){return r}});let r=(0,n(6583).Z)("Info",[["circle",{cx:"12",cy:"12",r:"10",key:"1mglay"}],["path",{d:"M12 16v-4",key:"1dtifu"}],["path",{d:"M12 8h.01",key:"e9boi3"}]])},7601:function(e,t,n){n.d(t,{VY:function(){return eE},h4:function(){return eh},ck:function(){return em},fC:function(){return ep},xz:function(){return ev}});var r=n(7462),l=n(7294),o=n.t(l,2);function i(e,t=[]){let n=[],r=()=>{let t=n.map(e=>(0,l.createContext)(e));return function(n){let r=(null==n?void 0:n[e])||t;return(0,l.useMemo)(()=>({[`__scope${e}`]:{...n,[e]:r}}),[n,r])}};return r.scopeName=e,[function(t,r){let o=(0,l.createContext)(r),i=n.length;function a(t){let{scope:n,children:r,...a}=t,u=(null==n?void 0:n[e][i])||o,c=(0,l.useMemo)(()=>a,Object.values(a));return(0,l.createElement)(u.Provider,{value:c},r)}return n=[...n,r],a.displayName=t+"Provider",[a,function(n,a){let u=(null==a?void 0:a[e][i])||o,c=(0,l.useContext)(u);if(c)return c;if(void 0!==r)return r;throw Error(`\`${n}\` must be used within \`${t}\``)}]},function(...e){let t=e[0];if(1===e.length)return t;let n=()=>{let n=e.map(e=>({useScope:e(),scopeName:e.scopeName}));return function(e){let r=n.reduce((t,{useScope:n,scopeName:r})=>{let l=n(e)[`__scope${r}`];return{...t,...l}},{});return(0,l.useMemo)(()=>({[`__scope${t.scopeName}`]:r}),[r])}};return n.scopeName=t.scopeName,n}(r,...t)]}function a(...e){return t=>e.forEach(e=>{"function"==typeof e?e(t):null!=e&&(e.current=t)})}function u(...e){return(0,l.useCallback)(a(...e),e)}let c=(0,l.forwardRef)((e,t)=>{let{children:n,...o}=e,i=l.Children.toArray(n),a=i.find(f);if(a){let e=a.props.children,n=i.map(t=>t!==a?t:l.Children.count(e)>1?l.Children.only(null):(0,l.isValidElement)(e)?e.props.children:null);return(0,l.createElement)(d,(0,r.Z)({},o,{ref:t}),(0,l.isValidElement)(e)?(0,l.cloneElement)(e,void 0,n):null)}return(0,l.createElement)(d,(0,r.Z)({},o,{ref:t}),n)});c.displayName="Slot";let d=(0,l.forwardRef)((e,t)=>{let{children:n,...r}=e;return(0,l.isValidElement)(n)?(0,l.cloneElement)(n,{...function(e,t){let n={...t};for(let r in t){let l=e[r],o=t[r];/^on[A-Z]/.test(r)?l&&o?n[r]=(...e)=>{o(...e),l(...e)}:l&&(n[r]=l):"style"===r?n[r]={...l,...o}:"className"===r&&(n[r]=[l,o].filter(Boolean).join(" "))}return{...e,...n}}(r,n.props),ref:t?a(t,n.ref):n.ref}):l.Children.count(n)>1?l.Children.only(null):null});d.displayName="SlotClone";let s=({children:e})=>(0,l.createElement)(l.Fragment,null,e);function f(e){return(0,l.isValidElement)(e)&&e.type===s}function p(e,t,{checkForDefaultPrevented:n=!0}={}){return function(r){if(null==e||e(r),!1===n||!r.defaultPrevented)return null==t?void 0:t(r)}}function m(e){let t=(0,l.useRef)(e);return(0,l.useEffect)(()=>{t.current=e}),(0,l.useMemo)(()=>(...e)=>{var n;return null===(n=t.current)||void 0===n?void 0:n.call(t,...e)},[])}function h({prop:e,defaultProp:t,onChange:n=()=>{}}){let[r,o]=function({defaultProp:e,onChange:t}){let n=(0,l.useState)(e),[r]=n,o=(0,l.useRef)(r),i=m(t);return(0,l.useEffect)(()=>{o.current!==r&&(i(r),o.current=r)},[r,o,i]),n}({defaultProp:t,onChange:n}),i=void 0!==e,a=i?e:r,u=m(n);return[a,(0,l.useCallback)(t=>{if(i){let n="function"==typeof t?t(e):t;n!==e&&u(n)}else o(t)},[i,e,o,u])]}var v=n(3935);let E=(0,l.forwardRef)((e,t)=>{let{children:n,...o}=e,i=l.Children.toArray(n),a=i.find(C);if(a){let e=a.props.children,n=i.map(t=>t!==a?t:l.Children.count(e)>1?l.Children.only(null):(0,l.isValidElement)(e)?e.props.children:null);return(0,l.createElement)(y,(0,r.Z)({},o,{ref:t}),(0,l.isValidElement)(e)?(0,l.cloneElement)(e,void 0,n):null)}return(0,l.createElement)(y,(0,r.Z)({},o,{ref:t}),n)});E.displayName="Slot";let y=(0,l.forwardRef)((e,t)=>{let{children:n,...r}=e;return(0,l.isValidElement)(n)?(0,l.cloneElement)(n,{...function(e,t){let n={...t};for(let r in t){let l=e[r],o=t[r];/^on[A-Z]/.test(r)?l&&o?n[r]=(...e)=>{o(...e),l(...e)}:l&&(n[r]=l):"style"===r?n[r]={...l,...o}:"className"===r&&(n[r]=[l,o].filter(Boolean).join(" "))}return{...e,...n}}(r,n.props),ref:t?a(t,n.ref):n.ref}):l.Children.count(n)>1?l.Children.only(null):null});y.displayName="SlotClone";let b=({children:e})=>(0,l.createElement)(l.Fragment,null,e);function C(e){return(0,l.isValidElement)(e)&&e.type===b}let g=["a","button","div","form","h2","h3","img","input","label","li","nav","ol","p","span","svg","ul"].reduce((e,t)=>{let n=(0,l.forwardRef)((e,n)=>{let{asChild:o,...i}=e,a=o?E:t;return(0,l.useEffect)(()=>{window[Symbol.for("radix-ui")]=!0},[]),(0,l.createElement)(a,(0,r.Z)({},i,{ref:n}))});return n.displayName=`Primitive.${t}`,{...e,[t]:n}},{}),w=(null==globalThis?void 0:globalThis.document)?l.useLayoutEffect:()=>{},A=e=>{let{present:t,children:n}=e,r=function(e){var t,n;let[r,o]=(0,l.useState)(),i=(0,l.useRef)({}),a=(0,l.useRef)(e),u=(0,l.useRef)("none"),[c,d]=(t=e?"mounted":"unmounted",n={mounted:{UNMOUNT:"unmounted",ANIMATION_OUT:"unmountSuspended"},unmountSuspended:{MOUNT:"mounted",ANIMATION_END:"unmounted"},unmounted:{MOUNT:"mounted"}},(0,l.useReducer)((e,t)=>{let r=n[e][t];return null!=r?r:e},t));return(0,l.useEffect)(()=>{let e=N(i.current);u.current="mounted"===c?e:"none"},[c]),w(()=>{let t=i.current,n=a.current;if(n!==e){let r=u.current,l=N(t);e?d("MOUNT"):"none"===l||(null==t?void 0:t.display)==="none"?d("UNMOUNT"):n&&r!==l?d("ANIMATION_OUT"):d("UNMOUNT"),a.current=e}},[e,d]),w(()=>{if(r){let e=e=>{let t=N(i.current).includes(e.animationName);e.target===r&&t&&(0,v.flushSync)(()=>d("ANIMATION_END"))},t=e=>{e.target===r&&(u.current=N(i.current))};return r.addEventListener("animationstart",t),r.addEventListener("animationcancel",e),r.addEventListener("animationend",e),()=>{r.removeEventListener("animationstart",t),r.removeEventListener("animationcancel",e),r.removeEventListener("animationend",e)}}d("ANIMATION_END")},[r,d]),{isPresent:["mounted","unmountSuspended"].includes(c),ref:(0,l.useCallback)(e=>{e&&(i.current=getComputedStyle(e)),o(e)},[])}}(t),o="function"==typeof n?n({present:r.isPresent}):l.Children.only(n),i=u(r.ref,o.ref);return"function"==typeof n||r.isPresent?(0,l.cloneElement)(o,{ref:i}):null};function N(e){return(null==e?void 0:e.animationName)||"none"}A.displayName="Presence";let _=o["useId".toString()]||(()=>void 0),R=0;function I(e){let[t,n]=l.useState(_());return w(()=>{e||n(e=>null!=e?e:String(R++))},[e]),e||(t?`radix-${t}`:"")}let k="Collapsible",[M,x]=i(k),[S,O]=M(k),Z=(0,l.forwardRef)((e,t)=>{let{__scopeCollapsible:n,open:o,defaultOpen:i,disabled:a,onOpenChange:u,...c}=e,[d=!1,s]=h({prop:o,defaultProp:i,onChange:u});return(0,l.createElement)(S,{scope:n,disabled:a,contentId:I(),open:d,onOpenToggle:(0,l.useCallback)(()=>s(e=>!e),[s])},(0,l.createElement)(g.div,(0,r.Z)({"data-state":U(d),"data-disabled":a?"":void 0},c,{ref:t})))}),T=(0,l.forwardRef)((e,t)=>{let{__scopeCollapsible:n,...o}=e,i=O("CollapsibleTrigger",n);return(0,l.createElement)(g.button,(0,r.Z)({type:"button","aria-controls":i.contentId,"aria-expanded":i.open||!1,"data-state":U(i.open),"data-disabled":i.disabled?"":void 0,disabled:i.disabled},o,{ref:t,onClick:p(e.onClick,i.onOpenToggle)}))}),P="CollapsibleContent",V=(0,l.forwardRef)((e,t)=>{let{forceMount:n,...o}=e,i=O(P,e.__scopeCollapsible);return(0,l.createElement)(A,{present:n||i.open},({present:e})=>(0,l.createElement)(D,(0,r.Z)({},o,{ref:t,present:e})))}),D=(0,l.forwardRef)((e,t)=>{let{__scopeCollapsible:n,present:o,children:i,...a}=e,c=O(P,n),[d,s]=(0,l.useState)(o),f=(0,l.useRef)(null),p=u(t,f),m=(0,l.useRef)(0),h=m.current,v=(0,l.useRef)(0),E=v.current,y=c.open||d,b=(0,l.useRef)(y),C=(0,l.useRef)();return(0,l.useEffect)(()=>{let e=requestAnimationFrame(()=>b.current=!1);return()=>cancelAnimationFrame(e)},[]),w(()=>{let e=f.current;if(e){C.current=C.current||{transitionDuration:e.style.transitionDuration,animationName:e.style.animationName},e.style.transitionDuration="0s",e.style.animationName="none";let t=e.getBoundingClientRect();m.current=t.height,v.current=t.width,b.current||(e.style.transitionDuration=C.current.transitionDuration,e.style.animationName=C.current.animationName),s(o)}},[c.open,o]),(0,l.createElement)(g.div,(0,r.Z)({"data-state":U(c.open),"data-disabled":c.disabled?"":void 0,id:c.contentId,hidden:!y},a,{ref:p,style:{"--radix-collapsible-content-height":h?`${h}px`:void 0,"--radix-collapsible-content-width":E?`${E}px`:void 0,...e.style}}),y&&i)});function U(e){return e?"open":"closed"}let $=(0,l.createContext)(void 0),L="Accordion",F=["Home","End","ArrowDown","ArrowUp","ArrowLeft","ArrowRight"],[j,q,z]=function(e){let t=e+"CollectionProvider",[n,r]=i(t),[o,a]=n(t,{collectionRef:{current:null},itemMap:new Map}),d=e+"CollectionSlot",s=l.forwardRef((e,t)=>{let{scope:n,children:r}=e,o=u(t,a(d,n).collectionRef);return l.createElement(c,{ref:o},r)}),f=e+"CollectionItemSlot",p="data-radix-collection-item";return[{Provider:e=>{let{scope:t,children:n}=e,r=l.useRef(null),i=l.useRef(new Map).current;return l.createElement(o,{scope:t,itemMap:i,collectionRef:r},n)},Slot:s,ItemSlot:l.forwardRef((e,t)=>{let{scope:n,children:r,...o}=e,i=l.useRef(null),d=u(t,i),s=a(f,n);return l.useEffect(()=>(s.itemMap.set(i,{ref:i,...o}),()=>void s.itemMap.delete(i))),l.createElement(c,{[p]:"",ref:d},r)})},function(t){let n=a(e+"CollectionConsumer",t);return l.useCallback(()=>{let e=n.collectionRef.current;if(!e)return[];let t=Array.from(e.querySelectorAll(`[${p}]`));return Array.from(n.itemMap.values()).sort((e,n)=>t.indexOf(e.ref.current)-t.indexOf(n.ref.current))},[n.collectionRef,n.itemMap])},r]}(L),[B,H]=i(L,[z,x]),K=x(),Y=l.forwardRef((e,t)=>{let{type:n,...o}=e;return l.createElement(j.Provider,{scope:e.__scopeAccordion},"multiple"===n?l.createElement(ee,(0,r.Z)({},o,{ref:t})):l.createElement(X,(0,r.Z)({},o,{ref:t})))});Y.propTypes={type(e){let t=e.value||e.defaultValue;return e.type&&!["single","multiple"].includes(e.type)?Error("Invalid prop `type` supplied to `Accordion`. Expected one of `single | multiple`."):"multiple"===e.type&&"string"==typeof t?Error("Invalid prop `type` supplied to `Accordion`. Expected `single` when `defaultValue` or `value` is type `string`."):"single"===e.type&&Array.isArray(t)?Error("Invalid prop `type` supplied to `Accordion`. Expected `multiple` when `defaultValue` or `value` is type `string[]`."):null}};let[G,J]=B(L),[Q,W]=B(L,{collapsible:!1}),X=l.forwardRef((e,t)=>{let{value:n,defaultValue:o,onValueChange:i=()=>{},collapsible:a=!1,...u}=e,[c,d]=h({prop:n,defaultProp:o,onChange:i});return l.createElement(G,{scope:e.__scopeAccordion,value:c?[c]:[],onItemOpen:d,onItemClose:l.useCallback(()=>a&&d(""),[a,d])},l.createElement(Q,{scope:e.__scopeAccordion,collapsible:a},l.createElement(er,(0,r.Z)({},u,{ref:t}))))}),ee=l.forwardRef((e,t)=>{let{value:n,defaultValue:o,onValueChange:i=()=>{},...a}=e,[u=[],c]=h({prop:n,defaultProp:o,onChange:i}),d=l.useCallback(e=>c((t=[])=>[...t,e]),[c]),s=l.useCallback(e=>c((t=[])=>t.filter(t=>t!==e)),[c]);return l.createElement(G,{scope:e.__scopeAccordion,value:u,onItemOpen:d,onItemClose:s},l.createElement(Q,{scope:e.__scopeAccordion,collapsible:!0},l.createElement(er,(0,r.Z)({},a,{ref:t}))))}),[et,en]=B(L),er=l.forwardRef((e,t)=>{let{__scopeAccordion:n,disabled:o,dir:i,orientation:a="vertical",...c}=e,d=u(l.useRef(null),t),s=q(n),f="ltr"===function(e){let t=(0,l.useContext)($);return e||t||"ltr"}(i),m=p(e.onKeyDown,e=>{var t;if(!F.includes(e.key))return;let n=e.target,r=s().filter(e=>{var t;return!(null!==(t=e.ref.current)&&void 0!==t&&t.disabled)}),l=r.findIndex(e=>e.ref.current===n),o=r.length;if(-1===l)return;e.preventDefault();let i=l,u=o-1,c=()=>{(i=l+1)>u&&(i=0)},d=()=>{(i=l-1)<0&&(i=u)};switch(e.key){case"Home":i=0;break;case"End":i=u;break;case"ArrowRight":"horizontal"===a&&(f?c():d());break;case"ArrowDown":"vertical"===a&&c();break;case"ArrowLeft":"horizontal"===a&&(f?d():c());break;case"ArrowUp":"vertical"===a&&d()}null===(t=r[i%o].ref.current)||void 0===t||t.focus()});return l.createElement(et,{scope:n,disabled:o,direction:i,orientation:a},l.createElement(j.Slot,{scope:n},l.createElement(g.div,(0,r.Z)({},c,{"data-orientation":a,ref:d,onKeyDown:o?void 0:m}))))}),el="AccordionItem",[eo,ei]=B(el),ea=l.forwardRef((e,t)=>{let{__scopeAccordion:n,value:o,...i}=e,a=en(el,n),u=J(el,n),c=K(n),d=I(),s=o&&u.value.includes(o)||!1,f=a.disabled||e.disabled;return l.createElement(eo,{scope:n,open:s,disabled:f,triggerId:d},l.createElement(Z,(0,r.Z)({"data-orientation":a.orientation,"data-state":ef(s)},c,i,{ref:t,disabled:f,open:s,onOpenChange:e=>{e?u.onItemOpen(o):u.onItemClose(o)}})))}),eu=l.forwardRef((e,t)=>{let{__scopeAccordion:n,...o}=e,i=en(L,n),a=ei("AccordionHeader",n);return l.createElement(g.h3,(0,r.Z)({"data-orientation":i.orientation,"data-state":ef(a.open),"data-disabled":a.disabled?"":void 0},o,{ref:t}))}),ec="AccordionTrigger",ed=l.forwardRef((e,t)=>{let{__scopeAccordion:n,...o}=e,i=en(L,n),a=ei(ec,n),u=W(ec,n),c=K(n);return l.createElement(j.ItemSlot,{scope:n},l.createElement(T,(0,r.Z)({"aria-disabled":a.open&&!u.collapsible||void 0,"data-orientation":i.orientation,id:a.triggerId},c,o,{ref:t})))}),es=l.forwardRef((e,t)=>{let{__scopeAccordion:n,...o}=e,i=en(L,n),a=ei("AccordionContent",n),u=K(n);return l.createElement(V,(0,r.Z)({role:"region","aria-labelledby":a.triggerId,"data-orientation":i.orientation},u,o,{ref:t,style:{"--radix-accordion-content-height":"var(--radix-collapsible-content-height)","--radix-accordion-content-width":"var(--radix-collapsible-content-width)",...e.style}}))});function ef(e){return e?"open":"closed"}let ep=Y,em=ea,eh=eu,ev=ed,eE=es}}]);