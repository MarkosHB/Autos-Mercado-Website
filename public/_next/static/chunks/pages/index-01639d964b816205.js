(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[405],{5557:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/",function(){return n(9828)}])},9828:function(e,t,n){"use strict";n.r(t),n.d(t,{Dialog__close_7f4e7e172c9e4494d2bff2343bebd255:function(){return L},Div_bd4c022a8f796682aa6392e9d4c102e9:function(){return T},Errorboundary_616e35b22bc2485638fce6192fdf8192:function(){return X},Fragment_27c482af64d0ff2d560fddd002da8a7d:function(){return N},Fragment_9017984ada32ffa55f5d2870ebd3c887:function(){return M},Root_8d0c186307264e049815924a6fdee47f:function(){return j},Segmentedcontrol__root_0988c85df014bfac5313cb27810cc06c:function(){return I},Toaster_6e6ebf8d7ce589d59b7d382fb7576edf:function(){return V},default:function(){return D}});var i=n(2729),r=n(5944),a=n(4511),o=n(7294),c=n(8039),s=n(9654),l=n(917),d=n(2658),h=n(3168),m=n(4949),u=n(4420),p=n(1700),f=n(6691),g=n(734),x=n(9531),Z=n(8007),v=n(4882),b=n(4712),w=n(3954),C=n(4390),F=n(4298),_=n.n(F),k=n(1664),S=n.n(k),y=n(7256),B=n(9008),H=n.n(B);function z(){let e=(0,i._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return z=function(){return e},e}function T(){let[e,t]=(0,o.useContext)(c.EventLoopContext);return(0,r.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: "+(t.length>0?t[t.length-1].message:""),children:(0,r.tZ)(M,{})})}function M(){let[e,t]=(0,o.useContext)(c.EventLoopContext);return(0,r.tZ)(o.Fragment,{children:(0,s.isTrue)(t.length>0)?(0,r.tZ)(o.Fragment,{children:(0,r.tZ)(d.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:E+" 1s infinite"},size:32})}):(0,r.tZ)(o.Fragment,{})})}function V(){let{resolvedColorMode:e}=(0,o.useContext)(c.ColorModeContext);s.refs.__toast=b.Am;let[t,n]=(0,o.useContext)(c.EventLoopContext),i={description:"Check if server is reachable at "+(0,s.getBackendURL)(w.Ks).href,closeButton:!0,duration:12e4,id:"websocket-error"},[a,l]=(0,o.useState)(!1);return(0,o.useEffect)(()=>{n.length>=2?a||b.Am.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...i,onDismiss:()=>l(!0)}):(b.Am.dismiss("websocket-error"),l(!1))},[n]),(0,r.tZ)(b.x7,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function X(){let[e,t]=(0,o.useContext)(c.EventLoopContext),n=(0,o.useCallback)((t,n)=>e([(0,s.Event)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:t.stack,component_stack:n.componentStack},{})],[t,n],{}),[e,s.Event]);return(0,r.BX)(a.SV,{fallbackRender:t=>(0,l.jsx)("div",{css:{height:"100%",width:"100%",position:"absolute",display:"flex",alignItems:"center",justifyContent:"center"}},(0,l.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem"}},(0,l.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem",maxWidth:"50ch",border:"1px solid #888888",borderRadius:"0.25rem",padding:"1rem"}},(0,l.jsx)("h2",{css:{fontSize:"1.25rem",fontWeight:"bold"}},(0,l.jsx)(o.Fragment,{},"An error occurred while rendering this page.")),(0,l.jsx)("p",{css:{opacity:"0.75"}},(0,l.jsx)(o.Fragment,{},"This is an error with the application itself.")),(0,l.jsx)("details",{},(0,l.jsx)("summary",{css:{padding:"0.5rem"}},(0,l.jsx)(o.Fragment,{},"Error message")),(0,l.jsx)("div",{css:{width:"100%",maxHeight:"50vh",overflow:"auto",background:"#000",color:"#fff",borderRadius:"0.25rem"}},(0,l.jsx)("div",{css:{padding:"0.5rem",width:"fit-content"}},(0,l.jsx)("pre",{},(0,l.jsx)(o.Fragment,{},t.error.stack)))),(0,l.jsx)("button",{css:{padding:"0.35rem 0.75rem",margin:"0.5rem",background:"#fff",color:"#000",border:"1px solid #000",borderRadius:"0.25rem",fontWeight:"bold"},onClick:function(){for(var n=arguments.length,i=Array(n),r=0;r<n;r++)i[r]=arguments[r];return e([(0,s.Event)("_call_function",{function:()=>navigator.clipboard.writeText(t.error.stack)},{})],i,{})}},(0,l.jsx)(o.Fragment,{},"Copy")))),(0,l.jsx)("hr",{css:{borderColor:"currentColor",opacity:"0.25"}}),(0,l.jsx)("a",{href:"https://reflex.dev"},(0,l.jsx)("div",{css:{display:"flex",alignItems:"baseline",justifyContent:"center",fontFamily:"monospace","--default-font-family":"monospace",gap:"0.5rem"}},(0,l.jsx)(o.Fragment,{},"Built with "),(0,l.jsx)("svg",{css:{viewBox:"0 0 56 12",fill:"currentColor"},height:"12",width:"56",xmlns:"http://www.w3.org/2000/svg"},(0,l.jsx)("path",{d:"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}),(0,l.jsx)("path",{d:"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}),(0,l.jsx)("path",{d:"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}),(0,l.jsx)("path",{d:"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}),(0,l.jsx)("path",{d:"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}),(0,l.jsx)("path",{d:"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"})))))),onError:n,children:[(0,r.BX)(o.Fragment,{children:[(0,r.tZ)(T,{}),(0,r.tZ)(V,{})]}),(0,r.BX)(C.Box,{children:[(0,r.tZ)(_(),{strategy:"afterInteractive",children:"document.documentElement.lang='es'"}),(0,r.tZ)(C.Flex,{align:"start",className:"rx-Stack",css:{background:"#010408",position:"sticky",paddingInlineStart:"2em",paddingInlineEnd:"2em",paddingTop:"1em",paddingBottom:"1em",zIndex:"999",top:"0",width:"100%"},direction:"column",gap:"3",children:(0,r.BX)(C.Flex,{align:"center",className:"rx-Stack",css:{width:"100%"},direction:"row",gap:"3",children:[(0,r.tZ)("img",{alt:"Logotipo de Autos-mercado.",src:"/logo.png"}),(0,r.tZ)(C.Flex,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,r.tZ)(C.Box,{css:{width:"100%",padding:"2em","@media screen and (min-width: 0)":{display:"none"},"@media screen and (min-width: 30em)":{display:"none"},"@media screen and (min-width: 48em)":{display:"none"},"@media screen and (min-width: 62em)":{display:"block"}},children:(0,r.BX)(C.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"6",children:[(0,r.tZ)(C.Flex,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"rgb(255, 45, 45)"},datatext:"Inicio",children:"Inicio"})})}),(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/coches-a-la-carta",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"#FFFFFF"},datatext:"Coches a la carta",children:"Coches a la carta"})})}),(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/vendemos-su-vehiculo",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"#FFFFFF"},datatext:"Vendemos su veh\xedculo",children:"Vendemos su veh\xedculo"})})}),(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/sobre-nosotros",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"#FFFFFF"},datatext:"Sobre nosotros",children:"Sobre nosotros"})})}),(0,r.BX)(C.Dialog.Root,{css:{margin:"20px"},children:[(0,r.tZ)(C.Dialog.Trigger,{children:(0,r.tZ)(C.Button,{color:"blue",radius:"large",size:"3",variant:"solid",children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"#FFFFFF"},datatext:"Contacto",children:"Contacto"})})}),(0,r.tZ)(C.Dialog.Content,{children:(0,r.tZ)(C.Card,{size:"3",variant:"ghost",children:(0,r.BX)(C.Flex,{css:{width:"100%"},direction:"column",gap:"4",children:[(0,r.BX)(C.Flex,{align:"start",className:"rx-Stack",css:{height:"100%",alignItems:"center",width:"100%"},direction:"row",gap:"4",children:[(0,r.tZ)(C.Badge,{color:"blue",css:{padding:"0.65rem"},radius:"full",children:(0,r.tZ)(h.Z,{css:{color:"var(--current-color)"},size:32})}),(0,r.BX)(C.Flex,{align:"start",className:"rx-Stack",css:{height:"100%"},direction:"column",gap:"1",children:[(0,r.tZ)(C.Heading,{size:"4",weight:"bold",children:"Contacte con nuestro equipo"}),(0,r.tZ)(C.Text,{as:"p",size:"2",children:"Ind\xedquenos el motivo por el que nos escribe."})]})]}),(0,r.tZ)(j,{})]})})})]})]})}),(0,r.tZ)(C.Box,{css:{"@media screen and (min-width: 0)":{display:"block"},"@media screen and (min-width: 30em)":{display:"block"},"@media screen and (min-width: 48em)":{display:"block"},"@media screen and (min-width: 62em)":{display:"none"}},children:(0,r.BX)(C.DropdownMenu.Root,{children:[(0,r.tZ)(C.DropdownMenu.Trigger,{children:(0,r.tZ)(C.Flex,{children:(0,r.tZ)(m.Z,{css:{color:"white"},size:40})})}),(0,r.BX)(C.DropdownMenu.Content,{css:{background:"#010408",borderColor:"#0C1116",minWidth:"100px"},children:[(0,r.tZ)(C.DropdownMenu.Item,{css:{background:"transparent"},children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"rgb(255, 45, 45)"},datatext:"Inicio",children:"Inicio"})})})}),(0,r.tZ)(C.DropdownMenu.Item,{css:{backbround:"transparent"},children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/coches-a-la-carta",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"#FFFFFF"},datatext:"Coches a la carta",children:"Coches a la carta"})})})}),(0,r.tZ)(C.DropdownMenu.Item,{css:{backbround:"transparent"},children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/vendemos-su-vehiculo",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"#FFFFFF"},datatext:"Vendemos su veh\xedculo",children:"Vendemos su veh\xedculo"})})})}),(0,r.tZ)(C.DropdownMenu.Item,{css:{backbround:"transparent"},children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/sobre-nosotros",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"#FFFFFF"},datatext:"Sobre nosotros",children:"Sobre nosotros"})})})}),(0,r.tZ)(C.DropdownMenu.Item,{css:{backbround:"transparent"},children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/contacto",passHref:!0,children:(0,r.tZ)(C.Text,{as:"p",css:{fontFamily:"Mona Sans","--default-font-family":"Mona Sans",fontWeight:"700","@media screen and (min-width: 0)":{fontSize:"1.5em"},color:"#FFFFFF"},datatext:"Contacto",children:"Contacto"})})})})]})]})})]})}),(0,r.tZ)(C.Flex,{css:{display:"flex",alignItems:"center",justifyContent:"center"},children:(0,r.BX)(C.Flex,{align:"center",className:"rx-Stack",css:{width:"100%"},direction:"column",gap:"5",children:[(0,r.BX)(C.Flex,{align:"center",className:"rx-Stack",css:{width:"100%",padding:"32px",background:"#010408"},direction:"column",gap:"3",children:[(0,r.tZ)("img",{css:{borderRadius:"20px 20px",border:"2px solid white"},src:"/fachada.jpg"}),(0,r.tZ)(C.Box,{css:{"@media screen and (min-width: 0)":{display:"none"},"@media screen and (min-width: 30em)":{display:"block"},"@media screen and (min-width: 48em)":{display:"block"},"@media screen and (min-width: 62em)":{display:"block"}},children:(0,r.BX)(C.Flex,{css:{borderTop:"1px solid #010408",padding:"2em",width:"100%",flexWrap:"wrap"},justify:"center",gap:"6",children:[(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(u.Z,{css:{color:"rgb(182, 209, 98)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"644 879 555"})]})})}),(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(u.Z,{css:{color:"rgb(182, 209, 98)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"688 483 324"})]})})}),(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(p.Z,{css:{color:"rgb(182, 209, 98)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"952 02 60 44"})]})})}),(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"mailto:autos-mercado@hotmail.com",passHref:!0,children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(f.Z,{css:{color:"rgb(188, 154, 250)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"autos-mercado@hotmail.com"})]})})})})]})})]}),(0,r.BX)(C.Flex,{align:"center",className:"rx-Stack",css:{width:"100%",padding:"1em"},direction:"column",gap:"4",children:[(0,r.tZ)(I,{}),(0,r.tZ)(C.Flex,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,r.tZ)(C.Blockquote,{color:"blue",size:"8",weight:"bold",children:"Descubra nuestro cat\xe1logo de veh\xedculos"})]}),(0,r.tZ)(N,{}),(0,r.BX)(C.Flex,{css:{background:"#010408",marginTop:"40px",borderTop:"1px solid #010408",padding:"2em",width:"100%",flexWrap:"wrap"},justify:"center",gap:"6",children:[(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(u.Z,{css:{color:"rgb(182, 209, 98)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"644 879 555"})]})})}),(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(u.Z,{css:{color:"rgb(182, 209, 98)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"688 483 324"})]})})}),(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(p.Z,{css:{color:"rgb(182, 209, 98)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"952 02 60 44"})]})})}),(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"mailto:autos-mercado@hotmail.com",passHref:!0,children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(f.Z,{css:{color:"rgb(188, 154, 250)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"autos-mercado@hotmail.com"})]})})})}),(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"https://www.instagram.com/autos_mercado/",passHref:!0,children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(g.Z,{css:{color:"rgb(245, 184, 165)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"@autos_mercado"})]})})})}),(0,r.tZ)(C.Button,{asChild:!0,css:{backgroundColor:"#0a0e12"},radius:"large",size:"3",variant:"surface",children:(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"https://www.facebook.com/people/Autos-Mercadocom/61553221770748/",passHref:!0,children:(0,r.BX)(C.Flex,{gap:"2",children:[(0,r.tZ)(x.Z,{css:{color:"rgb(130, 210, 207)"},size:20}),(0,r.tZ)(C.Text,{as:"p",size:"2",weight:"bold",children:"Autos-Mercado.com"})]})})})})]})]})})]}),(0,r.BX)(H(),{children:[(0,r.tZ)("title",{children:"Inicio | Autos-Mercado"}),(0,r.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}function j(){let[e,t]=(0,o.useContext)(c.EventLoopContext),n=(0,o.useCallback)(t=>{let n=t.target;t.preventDefault();let i={...Object.fromEntries(new FormData(n).entries())};!function(){for(var t=arguments.length,n=Array(t),r=0;r<t;r++)n[r]=arguments[r];e([(0,s.Event)("reflex___state____state.autosmercado___supabase____page_state____page_state.handle_submit",{form_data:i},{})],n,{})}(),n.reset()});return(0,r.tZ)(y.fC,{className:"Root ",css:{width:"100%"},onSubmit:n,children:(0,r.BX)(C.Flex,{css:{width:"100%"},direction:"column",gap:"2",children:[(0,r.BX)(C.Select.Root,{defaultValue:"Interesad@ en un veh\xedculo de Stock",name:"motivo",required:!0,children:[(0,r.tZ)(C.Select.Trigger,{}),(0,r.tZ)(C.Select.Content,{children:(0,r.BX)(C.Select.Group,{children:["",(0,r.tZ)(C.Select.Item,{value:"Interesad@ en un veh\xedculo de Stock",children:"Interesad@ en un veh\xedculo de Stock"}),(0,r.tZ)(C.Select.Item,{value:"Servicio: Coches a la carta",children:"Servicio: Coches a la carta"}),(0,r.tZ)(C.Select.Item,{value:"Servicio: Vendemos su veh\xedculo",children:"Servicio: Vendemos su veh\xedculo"}),(0,r.tZ)(C.Select.Item,{value:"Consulta adicional no contemplada",children:"Consulta adicional no contemplada"})]})})]}),(0,r.BX)(C.Flex,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"row"},"@media screen and (min-width: 48em)":{flexDirection:"row"}},gap:"3",children:[(0,r.tZ)(y.gN,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"nombre",children:(0,r.BX)(C.Flex,{direction:"column",gap:"1",children:[(0,r.tZ)(y.__,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Nombre."}),(0,r.tZ)(y.oT,{asChild:!0,className:"Control ",children:(0,r.tZ)(C.TextField.Root,{placeholder:"Su nombre de pila",type:"text"})})]})}),(0,r.tZ)(y.gN,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"apellidos",children:(0,r.BX)(C.Flex,{direction:"column",gap:"1",children:[(0,r.tZ)(y.__,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Apellidos."}),(0,r.tZ)(y.oT,{asChild:!0,className:"Control ",children:(0,r.tZ)(C.TextField.Root,{placeholder:"Su apellido completo",type:"text"})})]})})]}),(0,r.BX)(C.Flex,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"row"},"@media screen and (min-width: 48em)":{flexDirection:"row"}},gap:"3",children:[(0,r.tZ)(y.gN,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"email",children:(0,r.BX)(C.Flex,{direction:"column",gap:"1",children:[(0,r.tZ)(y.__,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Correo electr\xf3nico."}),(0,r.tZ)(y.oT,{asChild:!0,className:"Control ",children:(0,r.tZ)(C.TextField.Root,{placeholder:"Su email de uso habitual",type:"text"})})]})}),(0,r.tZ)(y.gN,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"telefono",children:(0,r.BX)(C.Flex,{direction:"column",gap:"1",children:[(0,r.tZ)(y.__,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Tel\xe9fono."}),(0,r.tZ)(y.oT,{asChild:!0,className:"Control ",children:(0,r.tZ)(C.TextField.Root,{placeholder:"Su n\xfamero de tel\xe9fono",type:"text"})})]})})]}),(0,r.BX)(C.Flex,{direction:"column",gap:"1",children:[(0,r.tZ)(C.Text,{as:"p",css:{"font-size":"15px","font-weight":"500","line-height":"35px"},children:"Mensaje."}),(0,r.tZ)(C.TextArea,{name:"mensaje",placeholder:"Motivo de contacto, datos relevantes...",resize:"vertical"})]}),(0,r.tZ)(y.k4,{className:"Submit ",css:{variant:"soft"},children:(0,r.tZ)(L,{})})]})})}function N(){let e=(0,o.useContext)(c.StateContexts.reflex___state____state__autosmercado___supabase____page_state____page_state);return(0,r.tZ)(o.Fragment,{children:(0,s.isTrue)(e.loading)?(0,r.tZ)(o.Fragment,{children:(0,r.tZ)(C.Flex,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:(0,r.tZ)(C.Flex,{css:{width:"100%",padding:"2em",flexWrap:"wrap"},justify:"center",children:(0,r.tZ)(C.Grid,{css:{gap:"2rem","@media screen and (min-width: 0)":{gridTemplateColumns:"1fr"},"@media screen and (min-width: 30em)":{gridTemplateColumns:"repeat(2, 1fr)"},"@media screen and (min-width: 48em)":{gridTemplateColumns:"repeat(2, 1fr)"},"@media screen and (min-width: 62em)":{gridTemplateColumns:"repeat(3, 1fr)"},"@media screen and (min-width: 80em)":{gridTemplateColumns:"repeat(4, 1fr)"},width:"100%"},gap:"4",children:(0,r.tZ)(r.HY,{children:Array.from({length:12},(e,t)=>0+1*t).map((e,t)=>(0,r.tZ)(C.Skeleton,{loading:!0,children:(0,r.BX)(C.Card,{css:{width:"100%",spacing:"4"},children:[(0,r.tZ)(C.Inset,{clip:"padding-box",pb:"current",side:"top",children:(0,r.tZ)(C.Text,{as:"p",css:{height:"250px"},children:"Placeholder"})}),(0,r.tZ)(C.Heading,{children:"Esto es un texto de prueba lo suficientemente largo ..."})]})},t))})})})})}):(0,r.tZ)(o.Fragment,{children:(0,r.tZ)(C.Flex,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:(0,r.tZ)(C.Flex,{css:{width:"100%",padding:"2em",flexWrap:"wrap"},justify:"center",children:(0,r.tZ)(C.Grid,{css:{gap:"2rem","@media screen and (min-width: 0)":{gridTemplateColumns:"1fr"},"@media screen and (min-width: 30em)":{gridTemplateColumns:"repeat(2, 1fr)"},"@media screen and (min-width: 48em)":{gridTemplateColumns:"repeat(2, 1fr)"},"@media screen and (min-width: 62em)":{gridTemplateColumns:"repeat(3, 1fr)"},"@media screen and (min-width: 80em)":{gridTemplateColumns:"repeat(4, 1fr)"},width:"100%"},gap:"4",children:(0,r.tZ)(r.HY,{children:e.vehiculos_info.map((e,t)=>(0,r.BX)(C.Card,{css:{width:"100%",spacing:"4"},children:[(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/detalles-del-vehiculo/"+e.url_modelo,passHref:!0,children:(0,r.tZ)(C.Inset,{clip:"padding-box",pb:"current",side:"top",children:(0,r.tZ)("img",{css:{width:"100%",height:"auto"},src:e.imagen_public_url})})})}),(0,r.BX)(C.Flex,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,r.tZ)(C.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,r.tZ)(S(),{href:"/detalles-del-vehiculo/"+e.url_modelo,passHref:!0,children:(0,r.tZ)(C.Heading,{children:e.modelo})})}),(0,r.tZ)(C.Separator,{size:"4"}),(0,r.tZ)(C.Flex,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,r.tZ)(C.Text,{align:"right",as:"p",size:"5",weight:"bold",children:e.precio_venta+" €"}),(0,r.tZ)(C.Text,{align:"center",as:"p",size:"3",weight:"medium",children:"Financiado por "+e.precio_financiado+" €/mes"})]})]},t))})})})})})})}function L(){let[e,t]=(0,o.useContext)(c.EventLoopContext),n=(0,o.useCallback)(function(){for(var t=arguments.length,n=Array(t),i=0;i<t;i++)n[i]=arguments[i];return e([(0,s.Event)("_call_function",{function:()=>s.refs.__toast.success("\xa1Formulario enviado correctamente!",{position:"bottom-right"})},{})],n,{})},[e,s.Event]);return(0,r.tZ)(C.Dialog.Close,{css:{width:"100%"},onClick:n,children:(0,r.tZ)(C.Button,{children:"Enviar informaci\xf3n"})})}function I(){let{setColorMode:e}=(0,o.useContext)(c.ColorModeContext),{rawColorMode:t}=(0,o.useContext)(c.ColorModeContext),[n,i]=(0,o.useContext)(c.EventLoopContext),a=(0,o.useCallback)(e,[n,s.Event,e]);return(0,r.BX)(C.SegmentedControl.Root,{onValueChange:a,radius:"large",value:t,variant:"classic",children:[(0,r.tZ)(C.SegmentedControl.Item,{value:"light",children:(0,r.tZ)(Z.Z,{css:{color:"var(--current-color)"},size:20})}),(0,r.tZ)(C.SegmentedControl.Item,{value:"dark",children:(0,r.tZ)(v.Z,{css:{color:"var(--current-color)"},size:20})})]})}let E=(0,l.keyframes)(z());function D(){return(0,r.tZ)(X,{})}}},function(e){e.O(0,[49,792,888,774,179],function(){return e(e.s=5557)}),_N_E=e.O()}]);