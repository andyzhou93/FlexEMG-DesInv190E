function data = load_FlexEMG_HDF(filename)
    if nargin < 1
        [name, path] = uigetfile('./data/hdfs/*.hdf');
        filename = [path name];
    end
    hdf = h5read(filename,'/dataGroup/dataTable');
    data = hdf.out;
    data = double(data(2:65,:)');
    
    crcs = find(hdf.out(1,:) ~= 0);
    for i = 1:length(crcs)
        data(crcs(i),:) = data(crcs(i)-1,:);
    end
end