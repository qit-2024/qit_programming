import React from 'react';  
import { Typography } from 'antd';  

const { Text } = Typography;  

interface MatrixDisplayProps {  
  matrix: number[][];  
  title?: string;  
}  

export const MatrixDisplay: React.FC<MatrixDisplayProps> = ({ matrix, title }) => {  
  return (  
    <div className="space-y-2">  
      {title && <Text strong>{title}</Text>}  
      <div className="grid gap-1">  
        {matrix.map((row, i) => (  
          <div key={i} className="flex gap-1">  
            {row.map((value, j) => (  
              <div  
                key={`${i}-${j}`}  
                className="w-14 h-14 flex items-center justify-center border border-gray-200 rounded bg-white"  
              >  
                <Text>{typeof value === 'number' ? value.toFixed(2) : value}</Text>  
              </div>  
            ))}  
          </div>  
        ))}  
      </div>  
    </div>  
  );  
};  