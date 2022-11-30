import { Tabs, Tab, Box, Button, Typography } from "@mui/material";
import { useState } from "react";
import TabPanel from "../../../components/panels/tabPanel";
import PanelConceptos from "./panels/panelConceptos";
const a11yProps = (index) => {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
};

export default () => {
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box
      sx={{
        width: "100vw",
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        p: 4,
      }}
    >
      <Box sx={{ width: "100%", display: "flex", mb: 2 }}>
        <Typography variant="h4" sx={{ fontWeight: "bold" }}>
          Gestión de Conceptos
        </Typography>
      </Box>
      <Box sx={{ width: "100%" }}>
        <Box>
          <Tabs
            value={value}
            onChange={handleChange}
            aria-label="basic tabs example"
          >
            <Tab label="Conceptos" {...a11yProps(0)} />
            <Tab label="Montos base" {...a11yProps(1)} />
            <Tab label="Bonificaciones" {...a11yProps(2)} />
            <Tab label="Recargos" {...a11yProps(3)} />
          </Tabs>
        </Box>
        <TabPanel value={value} index={0}>
          <PanelConceptos />
        </TabPanel>
      </Box>
    </Box>
  );
};
