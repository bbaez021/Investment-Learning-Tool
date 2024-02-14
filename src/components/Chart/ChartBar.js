import React from "react";

import "./ChartBar.css";
import PropTypes from "prop-types";

const ChartBar = (props) => {
  let barFillHeight = "0%";

  if (props.maxValue > 0) {
    barFillHeight = Math.round((props.value / props.maxValue) * 100) + "%";
  }
  return (
    <div className="chart-bar">
      <div className="chart-bar__inner">
        <div
          className="chart-bar__fill"
          style={{ height: barFillHeight }}
        ></div>
      </div>
      <div className="chart-bar__label">{props.label}</div>
    </div>
  );
};

ChartBar.propTypes = {
  maxValue: PropTypes.number,
  value: PropTypes.number,
  label: PropTypes.string,
};

export default ChartBar;
