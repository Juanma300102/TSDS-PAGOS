import { Box } from "@mui/system";
import {
  Button,
  Paper,
  TextField,
  Typography,
  FormControl,
} from "@mui/material";
import { Link, Outlet } from "react-router-dom";

export default () => {
  const textFieldSx = {
    m: 1,
  };

  return (
    <Box
      sx={{
        width: "100vw",
        height: "100vh",
        display: "inline-flex",
        justifyContent: "center",
        alignItems: "center",
        margin: 0,
        padding: 1,
        flexDirection: "column",
      }}
    >
      <Outlet />
    </Box>
  );
};
