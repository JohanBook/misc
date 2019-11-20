import React, { useState } from "react";
import Card from "@material-ui/core/Card";

export default function AnimatedCard(props) {
  const [raised, setRaised] = useState(false);

  return (
    <Card
      onClick={props.onClick}
      onMouseOver={() => setRaised(true)}
      onMouseOut={() => setRaised(false)}
      raised={raised}
      {...props}
    >
      {props.children}
    </Card>
  );
}
