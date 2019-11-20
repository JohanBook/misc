import React, { useRef } from "react";
import { Button, Container, Card, Col, Row } from "react-bootstrap";

export default function UploadButton(props) {
  const refDialog = useRef();

  function handleClick() {
    refDialog.current.click();
  }

  function handleUpload() {
    const file = refDialog.current.files[0];
    props.onClick(file);
  }

  return (
    <React.Fragment>
      <input
        id="none"
        type="file"
        ref={refDialog}
        accept={props.accept}
        onChange={handleUpload}
        hidden
      />
      <Button
        className={props.className}
        variant={props.variant}
        onClick={handleClick}
      >
        {props.text}
      </Button>
    </React.Fragment>
  );
}
