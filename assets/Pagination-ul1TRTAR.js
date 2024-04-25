import{r as V,k as st,f as R,u as x,R as i,B,t as it,a as ct,b as rt,i as lt,g as gt,h as mt,d as ut,m as dt,o as w}from"./index-B1Fa67u8.js";import{a as Pt,U as ht,g as pt,G as Z,S as vt}from"./Select-bYWseI_e.js";import"./polymorphic-factory-jpwrtp3F.js";function z(t,e){return n=>{t==null||t(n),e==null||e(n)}}function p(t,e){const n=e-t+1;return Array.from({length:n},(a,c)=>c+t)}const S="dots";function ft({total:t,siblings:e=1,boundaries:n=1,page:a,initialPage:c=1,onChange:o}){const s=Math.max(Math.trunc(t),0),[g,m]=Pt({value:a,onChange:o,defaultValue:c,finalValue:c}),r=f=>{f<=0?m(1):f>s?m(s):m(f)},u=()=>r(g+1),l=()=>r(g-1),P=()=>r(1),h=()=>r(s);return{range:V.useMemo(()=>{if(e*2+3+n*2>=s)return p(1,s);const _=Math.max(g-e,n),j=Math.min(g+e,s-n),I=_>n+2,N=j<s-(n+1);if(!I&&N){const C=e*2+n+2;return[...p(1,C),S,...p(s-(n-1),s)]}if(I&&!N){const C=n+1+2*e;return[...p(1,n),S,...p(s-C,s)]}return[...p(1,n),S,...p(_,j),S,...p(s-n+1,s)]},[s,e,g]),active:g,setPage:r,next:u,previous:l,first:P,last:h}}const[Ct,M]=st("Pagination.Root component was not found in tree");var y={root:"m_4addd315",control:"m_326d024a",dots:"m_4ad7767d"};const xt={withPadding:!0},L=R((t,e)=>{const n=x("PaginationControl",xt,t),{classNames:a,className:c,style:o,styles:s,vars:g,active:m,disabled:r,withPadding:u,mod:l,...P}=n,h=M(),v=r||h.disabled;return i.createElement(ht,{ref:e,disabled:v,mod:[{active:m,disabled:v,"with-padding":u},l],...h.getStyles("control",{className:c,style:o,classNames:a,styles:s,active:!v}),...P})});L.classes=y;L.displayName="@mantine/core/PaginationControl";function E({style:t,children:e,path:n,...a}){return i.createElement("svg",{viewBox:"0 0 16 16",xmlns:"http://www.w3.org/2000/svg",style:{width:"calc(var(--pagination-control-size) / 1.8)",height:"calc(var(--pagination-control-size) / 1.8)",...t},...a},i.createElement("path",{d:n,fill:"currentColor"}))}const yt=t=>i.createElement(E,{...t,path:"M8.781 8l-3.3-3.3.943-.943L10.667 8l-4.243 4.243-.943-.943 3.3-3.3z"}),Lt=t=>i.createElement(E,{...t,path:"M7.219 8l3.3 3.3-.943.943L5.333 8l4.243-4.243.943.943-3.3 3.3z"}),Et=t=>i.createElement(E,{...t,path:"M6.85355 3.85355C7.04882 3.65829 7.04882 3.34171 6.85355 3.14645C6.65829 2.95118 6.34171 2.95118 6.14645 3.14645L2.14645 7.14645C1.95118 7.34171 1.95118 7.65829 2.14645 7.85355L6.14645 11.8536C6.34171 12.0488 6.65829 12.0488 6.85355 11.8536C7.04882 11.6583 7.04882 11.3417 6.85355 11.1464L3.20711 7.5L6.85355 3.85355ZM12.8536 3.85355C13.0488 3.65829 13.0488 3.34171 12.8536 3.14645C12.6583 2.95118 12.3417 2.95118 12.1464 3.14645L8.14645 7.14645C7.95118 7.34171 7.95118 7.65829 8.14645 7.85355L12.1464 11.8536C12.3417 12.0488 12.6583 12.0488 12.8536 11.8536C13.0488 11.6583 13.0488 11.3417 12.8536 11.1464L9.20711 7.5L12.8536 3.85355Z"}),It=t=>i.createElement(E,{...t,path:"M2.14645 11.1464C1.95118 11.3417 1.95118 11.6583 2.14645 11.8536C2.34171 12.0488 2.65829 12.0488 2.85355 11.8536L6.85355 7.85355C7.04882 7.65829 7.04882 7.34171 6.85355 7.14645L2.85355 3.14645C2.65829 2.95118 2.34171 2.95118 2.14645 3.14645C1.95118 3.34171 1.95118 3.65829 2.14645 3.85355L5.79289 7.5L2.14645 11.1464ZM8.14645 11.1464C7.95118 11.3417 7.95118 11.6583 8.14645 11.8536C8.34171 12.0488 8.65829 12.0488 8.85355 11.8536L12.8536 7.85355C13.0488 7.65829 13.0488 7.34171 12.8536 7.14645L8.85355 3.14645C8.65829 2.95118 8.34171 2.95118 8.14645 3.14645C7.95118 3.34171 7.95118 3.65829 8.14645 3.85355L11.7929 7.5L8.14645 11.1464Z"}),Nt=t=>i.createElement(E,{...t,path:"M2 8c0-.733.6-1.333 1.333-1.333.734 0 1.334.6 1.334 1.333s-.6 1.333-1.334 1.333C2.6 9.333 2 8.733 2 8zm9.333 0c0-.733.6-1.333 1.334-1.333C13.4 6.667 14 7.267 14 8s-.6 1.333-1.333 1.333c-.734 0-1.334-.6-1.334-1.333zM6.667 8c0-.733.6-1.333 1.333-1.333s1.333.6 1.333 1.333S8.733 9.333 8 9.333 6.667 8.733 6.667 8z"}),wt={icon:Nt},b=R((t,e)=>{const n=x("PaginationDots",wt,t),{classNames:a,className:c,style:o,styles:s,vars:g,icon:m,...r}=n,u=M(),l=m;return i.createElement(B,{ref:e,...u.getStyles("dots",{className:c,style:o,styles:s,classNames:a}),...r},i.createElement(l,{style:{width:"calc(var(--pagination-control-size) / 1.8)",height:"calc(var(--pagination-control-size) / 1.8)"}}))});b.classes=y;b.displayName="@mantine/core/PaginationDots";function F({icon:t,name:e,action:n,type:a}){const c={icon:t},o=V.forwardRef((s,g)=>{const{icon:m,...r}=x(e,c,s),u=m,l=M(),P=a==="next"?l.active===l.total:l.active===1;return i.createElement(L,{disabled:l.disabled||P,ref:g,onClick:l[n],withPadding:!1,...r},i.createElement(u,{className:"mantine-rotate-rtl",style:{width:"calc(var(--pagination-control-size) / 1.8)",height:"calc(var(--pagination-control-size) / 1.8)"}}))});return o.displayName=`@mantine/core/${e}`,it(o)}const A=F({icon:yt,name:"PaginationNext",action:"onNext",type:"next"}),U=F({icon:Lt,name:"PaginationPrevious",action:"onPrevious",type:"previous"}),G=F({icon:Et,name:"PaginationFirst",action:"onFirst",type:"previous"}),T=F({icon:It,name:"PaginationLast",action:"onLast",type:"next"});function $({dotsIcon:t}){const e=M(),n=e.range.map((a,c)=>{var o;return a==="dots"?i.createElement(b,{icon:t,key:c}):i.createElement(L,{key:c,active:a===e.active,"aria-current":a===e.active?"page":void 0,onClick:()=>e.onChange(a),disabled:e.disabled,...(o=e.getItemProps)==null?void 0:o.call(e,a)},a)});return i.createElement(i.Fragment,null,n)}$.displayName="@mantine/core/PaginationItems";const zt={siblings:1,boundaries:1},St=rt((t,{size:e,radius:n,color:a,autoContrast:c})=>({root:{"--pagination-control-radius":n===void 0?void 0:lt(n),"--pagination-control-size":gt(e,"pagination-control-size"),"--pagination-control-fz":mt(e),"--pagination-active-bg":a?ut(a,t):void 0,"--pagination-active-color":pt(c,t)?dt({color:a,theme:t}):void 0}})),D=R((t,e)=>{const n=x("PaginationRoot",zt,t),{classNames:a,className:c,style:o,styles:s,unstyled:g,vars:m,total:r,value:u,defaultValue:l,onChange:P,disabled:h,siblings:v,boundaries:f,color:_,radius:j,onNextPage:I,onPreviousPage:N,onFirstPage:C,onLastPage:O,getItemProps:q,autoContrast:bt,...J}=n,k=ct({name:"Pagination",classes:y,props:n,className:c,style:o,classNames:a,styles:s,unstyled:g,vars:m,varsResolver:St}),{range:K,setPage:Q,next:W,previous:X,active:Y,first:H,last:tt}=ft({page:u,initialPage:l,onChange:P,total:r,siblings:v,boundaries:f}),et=z(I,W),nt=z(N,X),at=z(C,H),ot=z(O,tt);return i.createElement(Ct,{value:{total:r,range:K,active:Y,disabled:h,getItemProps:q,onChange:Q,onNext:et,onPrevious:nt,onFirst:at,onLast:ot,getStyles:k}},i.createElement(B,{ref:e,...k("root"),...J}))});D.classes=y;D.displayName="@mantine/core/PaginationRoot";const Rt={withControls:!0,siblings:1,boundaries:1,gap:8},d=R((t,e)=>{const n=x("Pagination",Rt,t),{withEdges:a,withControls:c,getControlProps:o,nextIcon:s,previousIcon:g,lastIcon:m,firstIcon:r,dotsIcon:u,total:l,gap:P,...h}=n;return l<=0?null:i.createElement(D,{ref:e,total:l,...h},i.createElement(Z,{gap:P},a&&i.createElement(G,{icon:r,...o==null?void 0:o("first")}),c&&i.createElement(U,{icon:g,...o==null?void 0:o("previous")}),i.createElement($,{dotsIcon:u}),c&&i.createElement(A,{icon:s,...o==null?void 0:o("next")}),a&&i.createElement(T,{icon:m,...o==null?void 0:o("last")})))});d.classes=y;d.displayName="@mantine/core/Pagination";d.Root=D;d.Control=L;d.Dots=b;d.First=G;d.Last=T;d.Next=A;d.Previous=U;d.Items=$;const Mt=({itemsPerPage:t,totalItems:e,paginate:n,currentPage:a,setItemsPerPage:c})=>{const o=Math.ceil(e/t);return w.jsx("nav",{"aria-label":"Era page navigation",children:w.jsxs(Z,{align:"center",style:{justifyContent:"space-between"},children:[w.jsx(d,{value:a,onChange:n,total:o,color:"blue",size:"sm"}),w.jsx(vt,{value:t.toString(),onChange:s=>c(Number(s)),data:[{value:"10",label:"10"},{value:"20",label:"20"},{value:"50",label:"50"}],style:{width:100}})]})})},jt=i.memo(Mt);export{jt as default};
