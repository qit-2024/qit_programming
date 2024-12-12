import React, { useState } from 'react';
import {
  TextField,
  Button,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Paper,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow
} from '@mui/material';

import { useAppDispatch, useAppSelector } from '../store/hooks';
import {
  setInputMatrix,
  updateMatrixCell,
  setDecompositionType,
  performDecomposition
} from '../store/matrixSlice';

const MatrixInput: React.FC = () => {
  const dispatch = useAppDispatch();
  const { inputMatrix, decompositionType } = useAppSelector(state => state.matrix);

  const [rows, setRows] = useState(2);
  const [cols, setCols] = useState(2);
 
  const [tempRows, setTempRows] = useState(2);
  const [tempCols, setTempCols] = useState(2);


  const [tempInput, setTempInput] = useState<{ [key: string]: string }>({});

  const handleMatrixChange = (rowIndex: number, colIndex: number, value: string) => {
    if (value === "-" || value === "") {  
      setTempInput((prev) => ({
        ...prev,
        [`${rowIndex}-${colIndex}`]: value,
      }));
      return;
    }

    const numValue = parseFloat(value);

    if (!isNaN(numValue)) {
      setTempInput((prev) => {
        const updated = { ...prev };
        delete updated[`${rowIndex}-${colIndex}`];
        return updated;
      });
 
      dispatch(updateMatrixCell({ rowIndex, colIndex, value: numValue }));
    }
  };

  const handleResize = () => {
    setRows(tempRows);
    setCols(tempCols);
 
    const newMatrix: number[][] = Array.from({ length: tempRows }, () =>
      Array.from({ length: tempCols }, () => 0)
    );
    dispatch(setInputMatrix(newMatrix));
  };

  const handleDecompose = () => {
    dispatch(performDecomposition({
      matrix: inputMatrix,
      type: decompositionType
    }));
  };

  return (
    <Paper elevation={3} sx={{ p: 3, mt: 2 }}>
      <Typography variant="h5" gutterBottom>
        Matrix Decomposition
      </Typography>

      <div style={{ display: 'flex', gap: '16px', marginBottom: '16px' }}>
        <TextField
          label="Rows"
          type="number"
          value={tempRows}
          onChange={(e) => setTempRows(parseInt(e.target.value))}
          slotProps={{
            htmlInput: { min: 1, max: 10 },
          }}
        />
        <TextField
          label="Columns"
          type="number"
          value={tempCols}
          onChange={(e) => setTempCols(parseInt(e.target.value))}
          slotProps={{
            htmlInput: { min: 1, max: 10 },
          }}
        />
        <Button variant="outlined" onClick={handleResize}>
          Resize Matrix
        </Button>
      </div>

      <TableContainer component={Paper} sx={{ mt: 2 }}>
        <Table>
          <TableHead>
            <TableRow>
              {Array.from({ length: cols }).map((_, colIndex) => (
                <TableCell key={colIndex} align="center">
                  Col {colIndex + 1}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {inputMatrix.map((row, rowIndex) => (
              <TableRow key={rowIndex}>
              
                {row.map((cell, colIndex) => (
                  <TableCell key={colIndex} align="center">
                    <TextField
                      type="text" // Use "text" to allow "-"  
                      value={
                        tempInput[`${rowIndex}-${colIndex}`] !== undefined
                          ? tempInput[`${rowIndex}-${colIndex}`]
                          : cell
                      }
                      onChange={(e) => handleMatrixChange(rowIndex, colIndex, e.target.value)}
                      variant="outlined"
                      size="small"
                      sx={{ width: 70 }}
                      slotProps={{
                        htmlInput: { min: -100, max: 100 },  
                      }}
                    />

                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <div style={{ display: 'flex', gap: '16px', marginTop: '16px' }}>
        <FormControl fullWidth>
          <InputLabel>Decomposition Type</InputLabel>
          <Select
            value={decompositionType}
            label="Decomposition Type"
            onChange={(e) => dispatch(setDecompositionType(e.target.value as 'LU' | 'QR'))}
          >
            <MenuItem value="LU">LU Decomposition</MenuItem>
            <MenuItem value="QR">QR Decomposition</MenuItem>
          </Select>
        </FormControl>
        <Button
          variant="contained"
          color="primary"
          onClick={handleDecompose}
          fullWidth
        >
          Decompose
        </Button>
      </div>
    </Paper>
  );
};

export default MatrixInput;