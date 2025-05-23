import React from 'react';
import Upload from './Upload';
import ReportPanel from './ReportPanel';

function App() {
  const [report, setReport] = React.useState("");
  const [image, setImage] = React.useState(null);

  return (
    <div style={{ display: "flex" }}>
      <div style={{ flex: 1 }}>
        <Upload setReport={setReport} setImage={setImage} />
        {image && <img src={image} alt="Annotated Result" width="100%" />}
      </div>
      <div style={{ flex: 1, padding: "1rem" }}>
        <ReportPanel report={report} />
      </div>
    </div>
  );
}

export default App;
