"use client";

import { useEffect } from "react";
import { Crisp } from "crisp-sdk-web";

export const CrispChat = () => {
  useEffect(() => {
    Crisp.configure("e9309e3f-7ecd-4c8b-8f03-4a1a7c9525a7");
  }, []);

  return null;
};
