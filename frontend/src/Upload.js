import React from 'react';
import axios from 'axios';

function Upload({ setReport, setImage }) {
  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://localhost:8000/upload/", formData);
    setReport(res.data.report);
    // Assume Roboflow returns URL or overlay this locally for demo
    setImage(URL.createObjectURL(file));
  };

  return (
    <div>
      <input type="file" accept=".dcm,.rvg" onChange={handleFileChange} />
    </div>
  );
}

export default Upload;
