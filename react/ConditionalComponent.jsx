import React from "react";

/* Only render component if condition is met */
export default function ConditionalComponent(props) {
  return props.condition ? <React.Fragment>{props.children}</React.Fragment> : null;
}
