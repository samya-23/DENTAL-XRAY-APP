import React from 'react';

function ReportPanel({ report }) {
  return (
    <div>
      <h3>Diagnostic Report</h3>
      <p>{report}</p>
    </div>
  );
}

export default ReportPanel;
