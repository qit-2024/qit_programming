import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';  
import axios from 'axios';  
import { EigenvaluesResponse, PropertiesResponse } from '../types/matrix';

const API_URL = 'http://localhost:8000';  

interface MatrixState {  
  loading: boolean;  
  error: string | null;  
  results: {  
    eigenvalues?: EigenvaluesResponse, 
    determinant?: number;  
    properties?: PropertiesResponse,
    tensor?: number[][];  
  };  
}  

const initialState: MatrixState = {  
  loading: false,  
  error: null,  
  results: {},  
};  

export const calculateEigenvalues = createAsyncThunk(  
  'matrix/eigenvalues',  
  async (matrix: number[][]) => {  
    const response = await axios.post(`${API_URL}/eigenvalues/`, { matrix });  
    return response.data;  
  }  
);  

export const calculateDeterminant = createAsyncThunk(  
  'matrix/determinant',  
  async (matrix: number[][]) => {  
    const response = await axios.post(`${API_URL}/determinant/`, { matrix });  
    return response.data;  
  }  
);  

export const checkProperties = createAsyncThunk(  
  'matrix/properties',  
  async (matrix: number[][]) => {  
    const response = await axios.post(`${API_URL}/properties/`, { matrix });  
    return response.data;  
  }  
);  

export const calculateTensorProduct = createAsyncThunk(  
  'matrix/tensor',  
  async ({ matrix_a, matrix_b }: { matrix_a: number[][], matrix_b: number[][] }) => {  
    const response = await axios.post(`${API_URL}/tensor/`, { matrix_a, matrix_b });  
    return response.data;  
  }  
);  

const matrixSlice = createSlice({  
  name: 'matrix',  
  initialState,  
  reducers: {  
    clearResults: (state) => {  
      state.results = {};  
    },  
  },  
  extraReducers: (builder) => {  
    builder  
      .addCase(calculateEigenvalues.pending, (state) => {  
        state.loading = true;  
        state.error = null;  
      })  
      .addCase(calculateEigenvalues.fulfilled, (state, action) => {  
        state.loading = false;  
        state.results = { ...state.results, eigenvalues: action.payload };  
      })  
      .addCase(calculateEigenvalues.rejected, (state, action) => {  
        state.loading = false;  
        state.error = action.error.message || 'Error';  
      })  
      // Аналогично для остальных операций  
  },  
});  

export const { clearResults } = matrixSlice.actions;  
export default matrixSlice.reducer;  