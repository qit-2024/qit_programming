// src/services/quantumService.ts  
import axios from 'axios';  
import { ComplexNumber, DensityMatrixResponse, DensityMatrixResult } from '../types/quantum';  

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';  

const transformResponse = (response: DensityMatrixResponse): DensityMatrixResult => {  
  return {  
    densityMatrix: response.density_matrix,  
    properties: {  
      trace: response.properties.trace,  
      isHermitian: response.properties.is_hermitian,  
      isPositive: response.properties.is_positive,  
      purity: response.properties.purity  
    }  
  };  
};  

export const quantumService = {  
  async calculateDensityMatrix(  
    stateVector: (number | ComplexNumber)[],  
    isComplex: boolean = false  
  ): Promise<DensityMatrixResult> {  
    try {  
      const response = await axios.post<DensityMatrixResponse>(  
        `${API_BASE_URL}/density-matrix/`,  
        {  
          state_vector: stateVector,  
          is_complex: isComplex  
        }  
      );  
      return transformResponse(response.data);  
    } catch (error: any) {  
      throw error;  
    }  
  }  
};