/* Buttons that open a file dialog when clicked
 * and fires specified function on selected file */

import React from "react";
import PropTypes from "prop-types";
import uuid from "uuid/v4";

import { Button, Fab, Tooltip } from "@material-ui/core";
import PublishIcon from "@material-ui/icons/Publish";

import { ConditionalComponent } from "./Util.jsx";

function UploadButton(props) {
  const id = uuid();

  function handleChange(event) {
    const file = event.target.files[0];
    props.onClick(file);
  }

  const upload = (
    <input
      accept={props.accept}
      id={id}
      type="file"
      style={{ display: "none" }}
      onChange={handleChange}
    />
  );

  return (
    <ConditionalComponent condition={props.visible}>
      {upload}
      <label htmlFor={id}>
        <Tooltip title={props.tooltip} aria-label="upload">
          {props.children}
        </Tooltip>
      </label>
    </ConditionalComponent>
  );
}

export function FileUploadButton(props) {
  return (
    <UploadButton {...props}>
      <Button component="span" {...props.buttonProps}>
        {" "}
        {props.content}{" "}
      </Button>
    </UploadButton>
  );
}

export function FileUploadIconButton(props) {
  return (
    <UploadButton {...props}>
      <Fab color="primary" component="span">
        <PublishIcon />
      </Fab>
    </UploadButton>
  );
}

UploadButton.propTypes = {
  accept: PropTypes.string.isRequired,
  onClick: PropTypes.func.isRequired,
  tooltip: PropTypes.string.isRequired,
  visible: PropTypes.bool
};

UploadButton.defaultProps = {
  visible: true
};

FileUploadButton.propTypes = {
  ...UploadButton.proptypes,
  content: PropTypes.string.isRequired
};
