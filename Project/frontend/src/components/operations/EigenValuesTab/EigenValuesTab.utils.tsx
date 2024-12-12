import { EigenvaluesResponse } from "../../../types/matrix";

export const getEigenvaluesData = (responseData?: EigenvaluesResponse) => {
    if (!responseData) return [];
    if (!responseData.eigenvalues) return [];

    return responseData.eigenvalues.map((value: number, index: number) => ({
        key: index,
        index: index + 1,
        value: formatNumber(value),
    }));
}

export const getEigenvectorsData = (responseData?: EigenvaluesResponse) => {
    if (!responseData) return [];
    if (!responseData.eigenvalues) return [];

    const { eigenvectors } = responseData;

    const transposed = eigenvectors[0].map((_: any, colIndex: string | number) =>
        eigenvectors.map((row: { [x: string]: any; }) => row[colIndex])
    );

    return transposed.map((row: any[], index: number) => ({
        key: index,
        index: index + 1,
        ...row.reduce((acc, value, i) => ({
            ...acc,
            [`vector${i + 1}`]: formatNumber(value)
        }), {})
    }));
};

export const getEigenvectorColumns = (responseData?: EigenvaluesResponse) => {
    if (!responseData) return [];
    if (!responseData.eigenvalues) return [];

    const baseColumns = [{
        title: '№',
        dataIndex: 'index',
        key: 'index',
        width: 80,
    }];

    const vectorColumns = responseData.eigenvalues.map((_: any, index: number) => ({
        title: `v${index + 1}`,
        dataIndex: `vector${index + 1}`,
        key: `vector${index + 1}`,
        className: 'font-mono',
    }));

    return [...baseColumns, ...vectorColumns];
};

const formatNumber = (num: number): string => {
    return num.toFixed(4);
};