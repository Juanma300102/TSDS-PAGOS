import { Edit } from "@mui/icons-material";
import { Box, Button, TextField } from "@mui/material";
import { DataGrid, GridActionsCell } from "@mui/x-data-grid";

export default () => {
  const rows = [
    { id: 1, col1: "Hello", col2: "World" },
    { id: 2, col1: "DataGridPro", col2: "is Awesome" },
    { id: 3, col1: "MUI", col2: "is Amazing" },
  ];

  const columns = [
    {
      field: "action",
      headerName: "Acciones",
      renderCell: (params) => [
        <GridActionsCell
          icon={<Edit />}
          label="edit"
          color="primary"
          onClick={() => {
            console.log("click on edit");
          }}
        />,
      ],
    },
    { field: "col1", headerName: "Titulo" },
    { field: "col2", headerName: "Descripción" },
  ];
  return (
    <Box sx={{ width: "90%", height: "60vh" }}>
      <Box sx={{ width: "100%", display: "flex", justifyContent: "end" }}>
        <Box
          sx={{
            width: "40%",
            marginRight: 1,
            display: "flex",
            justifyContent: "end",
          }}
        >
          <Button sx={{ marginRight: 1 }} variant="outlined" color="secondary">
            Filtros
          </Button>
          <TextField
            sx={{ width: "100%", maxWidth: "350px" }}
            size="small"
            variant="outlined"
            label="Ingrese algo..."
          />
          <Button variant="contained" sx={{ marginLeft: 1 }}>
            Buscar
          </Button>
        </Box>
        <Box
          sx={{
            display: "flex",
            marginLeft: 1,
          }}
        >
          <Box sx={{ display: "flex", margin: 0, p: 0 }}>
            <Button sx={{ marginLeft: 1 }} variant="contained" disableElevation>
              Crear
            </Button>
          </Box>
        </Box>
      </Box>
      <Box sx={{ width: "100%", marginTop: 2 }}>
        <DataGrid sx={{ height: "50vh" }} rows={rows} columns={columns} />
      </Box>
    </Box>
  );
};
