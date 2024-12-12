export interface MatrixState {
  loading: boolean;
  error: string | null;
  results: {
    eigenvalues?: {
      eigenvalues: number[];
      eigenvectors: number[][];
    };
    determinant?: number;
    properties?: {
      is_symmetric: boolean;
      is_orthogonal: boolean;
    };
    tensor?: number[][];
  };
}

export type Matrix = number[][];

export interface MatrixOperationError {
  message: string;
  status?: number;
  details?: any;
}

export interface MatrixOperation {
  type: string;
  matrix: number[][];
}

export interface TensorProductOperation {
  matrix_a: number[][];
  matrix_b: number[][];
}

// Добавим типы для ответов API
export interface EigenvaluesResponse {
  eigenvalues: number[];
  eigenvectors: number[][];
}

export interface DeterminantResponse {
  determinant: number;
}

export interface PropertiesResponse {
  is_symmetric: boolean;
  is_orthogonal: boolean;
}

export interface TensorProductResponse {
  result: number[][];
}
export interface MatrixProperties {  
  is_symmetric: boolean;  
  is_orthogonal: boolean;  
}  
