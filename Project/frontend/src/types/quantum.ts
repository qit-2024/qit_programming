export interface ComplexNumber {  
  real: number;  
  imag: number;  
}  

// Тип ответа от API  
export interface DensityMatrixResponse {  
  density_matrix: ComplexNumber[][];  
  properties: {  
    trace: number;  
    is_hermitian: boolean;  
    is_positive: boolean;  
    purity: number;  
  };  
}  

// Тип для использования во фронтенде  
export interface DensityMatrixResult {  
  densityMatrix: ComplexNumber[][];  
  properties: {  
    trace: number;  
    isHermitian: boolean;  
    isPositive: boolean;  
    purity: number;  
  };  
}  
