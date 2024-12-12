import { configureStore } from '@reduxjs/toolkit';  
import matrixReducer from './matrixSlice';  

export const store = configureStore({  
  reducer: {  
    matrix: matrixReducer,  
  },  
});  

export type RootState = ReturnType<typeof store.getState>;  
export type AppDispatch = typeof store.dispatch;  