import React, { useState } from "react";

import Container from "@material-ui/core/Container";
import Typography from "@material-ui/core/Typography";
import Slider from "@material-ui/core/Slider";

export default function ImageOverlay() {
  const width = 500;
  const height = 500;

  const [opacity, setOpacity] = useState(0);

  return (
    <Container>
      <div align="center">
        <Typography color="primary" variant="h5" gutterBottom>
          Image overlay
        </Typography>

        <img
          src="https://image.freepik.com/free-photo/image-human-brain_99433-298.jpg"
          alt=""
          width={width}
          height={height}
          style={{ position: "absolute", opacity: opacity }}
        />
        <img
          src="https://as.ftcdn.net/r/v1/pics/7b11b8176a3611dbfb25406156a6ef50cd3a5009/home/discover_collections/optimized/image-2019-10-11-11-36-27-681.jpg"
          alt=""
          width={width}
          height={height}
        />
      </div>
      <Slider
        value={opacity}
        aria-labelledby="continuous-slider"
        step={0.1}
        min={0}
        max={1}
        onChange={(_, v) => setOpacity(v)}
      />
    </Container>
  );
}
