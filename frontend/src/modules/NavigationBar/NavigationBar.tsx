import React, { useState } from "react";
import "./NavigationBar.css";

import ToggleAsideButton from "./ToggleAsideButton";

const NavigationBar = () => {
  const [isOpened, setIsOpened] = useState(false);

  return (
    <div>
      <ToggleAsideButton isOpened={isOpened} setIsOpened={setIsOpened} />
      <div
        className={` bg-black w-[100vw] h-[100vh] fixed z-50 transition-all animate-duration-800 ${
          isOpened ? " opacity-100" : "opacity-0"
        }`}
      ></div>
      <nav
        className={` w-72 h-[100vh] bg-[var(--md-sys-color-inverse-primary)] fixed z-[100] transition-all ${isOpened ? " left-0" : " -left-72"}`}
      >

      </nav>
    </div>
  );
};

export default NavigationBar;
