import{u as x,a as f,R as d,B as y,b as I,i as M,p as W,h as J,q as K,s as Q,d as X,r as P,f as Y,j as B,g as tt,k as et,_ as t,o as c,T as st,G as at}from"./index-CBSvmlmE.js";import{p as D}from"./polymorphic-factory-CMjoll_e.js";var F={root:"m_1b7284a3"};const rt={},ot=I((e,{radius:s,shadow:a})=>({root:{"--paper-radius":s===void 0?void 0:M(s),"--paper-shadow":W(a)}})),k=D((e,s)=>{const a=x("Paper",rt,e),{classNames:o,className:n,style:r,styles:_,unstyled:i,withBorder:u,vars:l,radius:m,shadow:E,variant:g,mod:R,...p}=a,v=f({name:"Paper",props:a,classes:F,className:n,style:r,classNames:o,styles:_,unstyled:i,vars:l,varsResolver:ot});return d.createElement(y,{ref:s,mod:[{"data-with-border":u},R],...v("root"),variant:g,...p})});k.classes=F;k.displayName="@mantine/core/Paper";var Z={root:"m_b6d8b162"};function nt(e){if(e==="start")return"start";if(e==="end"||e)return"end"}const _t={inherit:!1},it=I((e,{variant:s,lineClamp:a,gradient:o,size:n,color:r})=>({root:{"--text-fz":J(n),"--text-lh":K(n),"--text-gradient":s==="gradient"?Q(o,e):void 0,"--text-line-clamp":typeof a=="number"?a.toString():void 0,"--text-color":r?X(r,e):void 0}})),A=D((e,s)=>{const a=x("Text",_t,e),{lineClamp:o,truncate:n,inline:r,inherit:_,gradient:i,span:u,__staticSelector:l,vars:m,className:E,style:g,classNames:R,styles:p,unstyled:v,variant:h,mod:V,size:b,...w}=a,S=f({name:["Text",l],props:a,classes:Z,className:E,style:g,classNames:R,styles:p,unstyled:v,vars:m,varsResolver:it});return d.createElement(y,{...S("root",{focusable:!0}),ref:s,component:u?"span":"p",variant:h,mod:[{"data-truncate":nt(n),"data-line-clamp":typeof o=="number","data-inline":r,"data-inherit":_},V],size:b,...w})});A.classes=Z;A.displayName="@mantine/core/Text";const H=P.createContext(null),lt=H.Provider;function ct(){return{withinGroup:!!P.useContext(H)}}var C={group:"m_11def92b",root:"m_f85678b6",image:"m_11f8ac07",placeholder:"m_104cd71f"};const dt={},pt=I((e,{spacing:s})=>({group:{"--ag-spacing":B(s)}})),$=Y((e,s)=>{const a=x("AvatarGroup",dt,e),{classNames:o,className:n,style:r,styles:_,unstyled:i,vars:u,spacing:l,...m}=a,E=f({name:"AvatarGroup",classes:C,props:a,className:n,style:r,classNames:o,styles:_,unstyled:i,vars:u,varsResolver:pt,rootSelector:"group"});return d.createElement(lt,{value:!0},d.createElement(y,{ref:s,...E("group"),...m}))});$.classes=C;$.displayName="@mantine/core/AvatarGroup";function vt(e){return d.createElement("svg",{...e,"data-avatar-placeholder-icon":!0,viewBox:"0 0 15 15",fill:"none",xmlns:"http://www.w3.org/2000/svg"},d.createElement("path",{d:"M0.877014 7.49988C0.877014 3.84219 3.84216 0.877045 7.49985 0.877045C11.1575 0.877045 14.1227 3.84219 14.1227 7.49988C14.1227 11.1575 11.1575 14.1227 7.49985 14.1227C3.84216 14.1227 0.877014 11.1575 0.877014 7.49988ZM7.49985 1.82704C4.36683 1.82704 1.82701 4.36686 1.82701 7.49988C1.82701 8.97196 2.38774 10.3131 3.30727 11.3213C4.19074 9.94119 5.73818 9.02499 7.50023 9.02499C9.26206 9.02499 10.8093 9.94097 11.6929 11.3208C12.6121 10.3127 13.1727 8.97172 13.1727 7.49988C13.1727 4.36686 10.6328 1.82704 7.49985 1.82704ZM10.9818 11.9787C10.2839 10.7795 8.9857 9.97499 7.50023 9.97499C6.01458 9.97499 4.71624 10.7797 4.01845 11.9791C4.97952 12.7272 6.18765 13.1727 7.49985 13.1727C8.81227 13.1727 10.0206 12.727 10.9818 11.9787ZM5.14999 6.50487C5.14999 5.207 6.20212 4.15487 7.49999 4.15487C8.79786 4.15487 9.84999 5.207 9.84999 6.50487C9.84999 7.80274 8.79786 8.85487 7.49999 8.85487C6.20212 8.85487 5.14999 7.80274 5.14999 6.50487ZM7.49999 5.10487C6.72679 5.10487 6.09999 5.73167 6.09999 6.50487C6.09999 7.27807 6.72679 7.90487 7.49999 7.90487C8.27319 7.90487 8.89999 7.27807 8.89999 6.50487C8.89999 5.73167 8.27319 5.10487 7.49999 5.10487Z",fill:"currentColor",fillRule:"evenodd",clipRule:"evenodd"}))}const ut={},mt=I((e,{size:s,radius:a,variant:o,gradient:n,color:r,autoContrast:_})=>{const i=e.variantColorResolver({color:r||"gray",theme:e,gradient:n,variant:o||"light",autoContrast:_});return{root:{"--avatar-size":tt(s,"avatar-size"),"--avatar-radius":a===void 0?void 0:M(a),"--avatar-bg":r||o?i.background:void 0,"--avatar-color":r||o?i.color:void 0,"--avatar-bd":r||o?i.border:void 0}}}),L=D((e,s)=>{const a=x("Avatar",ut,e),{classNames:o,className:n,style:r,styles:_,unstyled:i,vars:u,src:l,alt:m,radius:E,color:g,gradient:R,imageProps:p,children:v,autoContrast:h,mod:V,...b}=a,w=ct(),[S,q]=P.useState(!l),N=f({name:"Avatar",props:a,classes:C,className:n,style:r,classNames:o,styles:_,unstyled:i,vars:u,varsResolver:mt});return P.useEffect(()=>q(!l),[l]),d.createElement(y,{...N("root"),mod:[{"within-group":w.withinGroup},V],ref:s,...b},S?d.createElement("span",{...N("placeholder"),title:m},v||d.createElement(vt,null)):d.createElement("img",{...p,...N("image"),src:l,alt:m,onError:U=>{var z;q(!0),(z=p==null?void 0:p.onError)==null||z.call(p,U)}}))});L.classes=C;L.displayName="@mantine/core/Avatar";L.Group=$;const[Et,gt]=et("Card component was not found in tree");var G={root:"m_e615b15f",section:"m_599a2148"};const Pt={},O=D((e,s)=>{const a=x("CardSection",Pt,e),{classNames:o,className:n,style:r,styles:_,vars:i,withBorder:u,inheritPadding:l,mod:m,...E}=a,g=gt();return d.createElement(y,{ref:s,mod:[{"with-border":u,"inherit-padding":l},m],...g.getStyles("section",{className:n,style:r,styles:_,classNames:o}),...E})});O.classes=G;O.displayName="@mantine/core/CardSection";const Rt={},At=I((e,{padding:s})=>({root:{"--card-padding":B(s)}})),T=D((e,s)=>{const a=x("Card",Rt,e),{classNames:o,className:n,style:r,styles:_,unstyled:i,vars:u,children:l,padding:m,...E}=a,g=f({name:"Card",props:a,classes:G,className:n,style:r,classNames:o,styles:_,unstyled:i,vars:u,varsResolver:At}),R=P.Children.toArray(l),p=R.map((v,h)=>typeof v=="object"&&v&&"type"in v&&v.type===O?P.cloneElement(v,{"data-first-section":h===0||void 0,"data-last-section":h===R.length-1||void 0}):v);return d.createElement(Et,{value:{getStyles:g}},d.createElement(k,{ref:s,unstyled:i,...g("root"),...E},p))});T.classes=G;T.displayName="@mantine/core/Card";T.Section=O;const yt=(e,s)=>{const a=e[s];return a?typeof a=="function"?a():Promise.resolve(a):new Promise((o,n)=>{(typeof queueMicrotask=="function"?queueMicrotask:setTimeout)(n.bind(null,new Error("Unknown variable dynamic import: "+s)))})},j={"custom-box":"_custom-box_bw602_12","quarter-circle":"_quarter-circle_bw602_58","quarter-circle-text":"_quarter-circle-text_bw602_84"},Tt={金:"white",木:"cyan",水:"black",火:"red",土:"#f2ce54"},xt={金:"black",木:"darkblue",水:"white",火:"white",土:"darkbrown"},ht="/chinese-era-explorer/assets/grunge-stained-old-paper-texture-DFM2vI4g.jpg",Dt=({era:e,emperor:s})=>{const a=e.element?Tt[e.element]:"transparent",o=e.element?xt[e.element]:"black",[n,r]=P.useState(null);return P.useEffect(()=>{yt(Object.assign({"../../assets/avatars/244.png":()=>t(()=>import("./244-CuNGm9pW.js"),[]),"../../assets/avatars/290.png":()=>t(()=>import("./290-DEY_hhBW.js"),[]),"../../assets/avatars/463.png":()=>t(()=>import("./463-XAXrIBUH.js"),[]),"../../assets/avatars/464.png":()=>t(()=>import("./464-B7S35UVO.js"),[]),"../../assets/avatars/465.png":()=>t(()=>import("./465-3I7jpG_T.js"),[]),"../../assets/avatars/466.png":()=>t(()=>import("./466-CRWDuvdS.js"),[]),"../../assets/avatars/467.png":()=>t(()=>import("./467-_f4T0fme.js"),[]),"../../assets/avatars/468.png":()=>t(()=>import("./468-DNa3FCfk.js"),[]),"../../assets/avatars/469.png":()=>t(()=>import("./469-Gkk-sH9L.js"),[]),"../../assets/avatars/470.png":()=>t(()=>import("./470-BMTB0sdg.js"),[]),"../../assets/avatars/471.png":()=>t(()=>import("./471-DyZT-t0X.js"),[]),"../../assets/avatars/480.png":()=>t(()=>import("./480-DpMtaD77.js"),[]),"../../assets/avatars/481.png":()=>t(()=>import("./481-BtcbxVhI.js"),[]),"../../assets/avatars/482.png":()=>t(()=>import("./482-BK_W9ScL.js"),[]),"../../assets/avatars/483.png":()=>t(()=>import("./483-DG1eTsQT.js"),[]),"../../assets/avatars/484.png":()=>t(()=>import("./484-D380VrUj.js"),[]),"../../assets/avatars/485.png":()=>t(()=>import("./485-4L5Htu12.js"),[]),"../../assets/avatars/561.png":()=>t(()=>import("./561-BjLeM_zF.js"),[]),"../../assets/avatars/562.png":()=>t(()=>import("./562-rE12JvcR.js"),[]),"../../assets/avatars/563.png":()=>t(()=>import("./563-B-OirouT.js"),[]),"../../assets/avatars/564.png":()=>t(()=>import("./564-lPY_MiiZ.js"),[]),"../../assets/avatars/568.png":()=>t(()=>import("./568-By9KT0oS.js"),[]),"../../assets/avatars/592.png":()=>t(()=>import("./592-DhQOE4Yk.js"),[]),"../../assets/avatars/594.png":()=>t(()=>import("./594-CTZuF_Dr.js"),[]),"../../assets/avatars/595.png":()=>t(()=>import("./595-CIR51I6u.js"),[]),"../../assets/avatars/596.png":()=>t(()=>import("./596-Cvy5qhxE.js"),[]),"../../assets/avatars/597.png":()=>t(()=>import("./597-CqVpY2d3.js"),[]),"../../assets/avatars/599.png":()=>t(()=>import("./599-CqVpY2d3.js"),[]),"../../assets/avatars/600.png":()=>t(()=>import("./600-D3ZBtFwe.js"),[]),"../../assets/avatars/601.png":()=>t(()=>import("./601-BuSzc5Dm.js"),[]),"../../assets/avatars/602.png":()=>t(()=>import("./602-sjYUlrJM.js"),[]),"../../assets/avatars/603.png":()=>t(()=>import("./603-CA8GDbzJ.js"),[]),"../../assets/avatars/604.png":()=>t(()=>import("./604-CDF7rz-e.js"),[]),"../../assets/avatars/605.png":()=>t(()=>import("./605-Qhxfk3b2.js"),[]),"../../assets/avatars/606.png":()=>t(()=>import("./606-cE3ceImK.js"),[]),"../../assets/avatars/607.png":()=>t(()=>import("./607-ByQKQk6u.js"),[]),"../../assets/avatars/662.png":()=>t(()=>import("./662-p26Jj2bN.js"),[]),"../../assets/avatars/663.png":()=>t(()=>import("./663-BNKRunG-.js"),[]),"../../assets/avatars/664.png":()=>t(()=>import("./664-BNKRunG-.js"),[]),"../../assets/avatars/665.png":()=>t(()=>import("./665-iiixj1lg.js"),[]),"../../assets/avatars/666.png":()=>t(()=>import("./666-2Aip4cwk.js"),[]),"../../assets/avatars/667.png":()=>t(()=>import("./667-B1JFfX7u.js"),[]),"../../assets/avatars/668.png":()=>t(()=>import("./668-Ca17LEji.js"),[]),"../../assets/avatars/669.png":()=>t(()=>import("./669-zK8M1EDF.js"),[]),"../../assets/avatars/670.png":()=>t(()=>import("./670-DEdA3pgG.js"),[]),"../../assets/avatars/671.png":()=>t(()=>import("./671-Czux9ijw.js"),[]),"../../assets/avatars/672.png":()=>t(()=>import("./672-B-ovYNn1.js"),[]),"../../assets/avatars/673.png":()=>t(()=>import("./673-Cul8Rs5l.js"),[]),"../../assets/avatars/674.png":()=>t(()=>import("./674-A7PiYBa1.js"),[])}),`../../assets/avatars/${s.id}.png`).then(_=>r(_.default)).catch(()=>r(null))},[s.id]),c.jsxs(y,{className:j["custom-box"],children:[c.jsxs(T,{shadow:"sm",radius:"md",style:{height:"100%",backgroundImage:`linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
            url(${ht})`,backgroundSize:"cover"},children:[c.jsx(T.Section,{inheritPadding:!0,mt:"md",style:{display:"flex",justifyContent:"center"},children:c.jsx(st,{order:1,style:{fontFamily:"標楷體",fontWeight:"bold",textAlign:"center"},children:e.name})}),e.start&&e.end&&c.jsxs(A,{size:"sm",ta:"center",mb:"md",children:["(",e.start," - ",e.end,")"]}),e.remark&&c.jsx(A,{mt:"md",pl:"md",pr:"md",children:e.remark}),s&&c.jsxs(T.Section,{inheritPadding:!0,withBorder:!0,pt:"md",pb:"xl",my:"md",mb:"xl",style:{borderTop:"2px solid black",padding:"16px"},children:[c.jsxs(at,{justify:"flex-start",pl:"md",pr:"md",children:[c.jsx(L,{src:n,alt:`${s.name}`,size:"lg"}),(s.title||s.name)&&c.jsxs(A,{size:"xl",children:[s.title," ",s.name]})]}),s.first_regnal_year&&s.final_regnal_year&&c.jsxs(A,{pl:"md",pr:"md",children:["在位時間: ",s.first_regnal_year," - ",s.final_regnal_year]})]})]}),c.jsx(y,{className:j["quarter-circle"],style:{backgroundColor:a},children:c.jsx(A,{className:j["quarter-circle-text"],style:{color:o},children:s.dynasty_name})})]})};export{Dt as default};