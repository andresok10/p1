import {Fragment,useContext,useEffect} from "react"
import {Box as RadixThemesBox,Button as RadixThemesButton,Flex as RadixThemesFlex} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent} from "$/utils/state"
import {jsx} from "@emotion/react"




function Flex_9d61bf47ace0049ccf1ca3a61d3c9b08 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "0.5rem", ["background"] : "gray.100" }),direction:"row",gap:"3"},Array.prototype.map.call(["Ecuabet", "Bilitv", "computrabajo", "Loteria", "DataBet", "Reflex"] ?? [],((site_name_rx_state_,index_cc691abb1629d5b4746ce0afe18b702a)=>(jsx(RadixThemesButton,{color:"blue",css:({ ["flex"] : "1" }),key:index_cc691abb1629d5b4746ce0afe18b702a,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.p1___p1____state.change_site", ({ ["site"] : site_name_rx_state_ }), ({  })))], [_e], ({  })))),size:"2",variant:"solid"},site_name_rx_state_)))))
  )
}


function Iframe_3eacbe90b5e996435a2295aeb4536a89 () {
  const reflex___state____state__p1___p1____state = useContext(StateContexts.reflex___state____state__p1___p1____state)



  return (
    jsx("iframe",{css:({ ["border"] : "none", ["width"] : "100%", ["height"] : "100%" }),src:reflex___state____state__p1___p1____state.current_url_rx_state_},)
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["height"] : "100vh", ["width"] : "100%", ["background"] : "white" }),direction:"column",gap:"0"},jsx(Flex_9d61bf47ace0049ccf1ca3a61d3c9b08,{},),jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["width"] : "100%" })},jsx(Iframe_3eacbe90b5e996435a2295aeb4536a89,{},))),jsx("title",{},"P1 | Index"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}