import { BrowserRouter, Routes, Route } from "react-router-dom";
import Landing from "./pages/landing";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="*" element={<h1>Pagina no encontrada</h1>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;