import { Box } from "@mui/system";
import {
  Button,
  Paper,
  TextField,
  Typography,
  FormControl,
} from "@mui/material";

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
        padding: 3,
        flexDirection: "column",
      }}
    >
      <Paper
        sx={{
          padding: 3,
          paddingX: 3,
          display: "flex",
          flexDirection: "column",
        }}
        elevation={5}
      >
        <FormControl>
          <Typography fontWeight="bold" textAlign="center" variant="h5">
            Iniciar Sesión
          </Typography>
          <Box
            sx={{
              display: "flex",
              flexDirection: "column",
              marginTop: 3,
            }}
          >
            <TextField
              sx={textFieldSx}
              id="email"
              label="Correo"
              variant="standard"
              type={"email"}
            />
            <TextField
              sx={textFieldSx}
              id="password"
              label="Contraseña"
              variant="standard"
              type={"password"}
            />
          </Box>
          <Box
            sx={{
              display: "flex",
              justifyContent: "space-between",
              padding: 0,
              margin: 0,
              marginTop: 3,
            }}
          >
            <Button variant="outlined">Registrarme</Button>
            <Button sx={{ marginLeft: 1 }} variant="contained">
              Entrar
            </Button>
          </Box>
          <Button sx={{ marginTop: 3 }}>Olvide mi contraseña</Button>
        </FormControl>
      </Paper>
      <Typography sx={{ marginTop: 2 }} color="primary" variant="body2">
        Terminos y condiciones de uso
      </Typography>
    </Box>
  );
};
