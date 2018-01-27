package ro.cs.ubbcluj.domain;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 * @author SERGIU Implementation of Pearson Correlation
 */
public class PearsonCorrelation {
	private Integer dataSetSize;
	private Entity<Integer> x;
	private Entity<Integer> y;

	public PearsonCorrelation(Integer dataSetSize, Entity x, Entity y) {
		super();
		this.dataSetSize = dataSetSize;
		this.x = x;
		this.y = y;
	}

	/**
	 * Compute x*y
	 * @return a list of x * y
	 */
	private List<Integer> getProductOfVariables() {
		List<Integer> product = new ArrayList<>();

		List<Integer> xValues = x.getFeatureList();
		List<Integer> yValues = y.getFeatureList();

		for (int i = 0; i < dataSetSize; i++) {
			int value = xValues.get(i) * yValues.get(i);
			product.add(value);
		}

		return product;
	}
	
	/**
	 * Compute each value of the entity at power 2
	 * @param variable with set of features
	 * @return list of each element at power 2
	 */
	private List<Integer>getValuesPow2(Entity variable){
		List<Integer>pow=new ArrayList<>();
		List<Integer>xValues = variable.getFeatureList();
		
		for(Integer value:xValues){
			int valueAtPow2 = value * value;
			pow.add(valueAtPow2);
		}
		
		return pow;
	}
	
	/**
	 * Computes Pearson Correlation Coefficient
	 * @return r - pearson correlation
	 */
	public Double getPearsonCorrelation(){
		List<Integer>xValues = x.getFeatureList();
		List<Integer>yValues = y.getFeatureList();
		List<Integer>xy = getProductOfVariables();
		List<Integer>xPow2 = getValuesPow2(x);
		List<Integer>yPow2 = getValuesPow2(y);
		
		int sumX = xValues.stream().mapToInt(i->i).sum();
		int sumY = yValues.stream().mapToInt(i->i).sum();
		int sumXY = xy.stream().mapToInt(i->i).sum();
		int sumXpow2 = xPow2.stream().mapToInt(i->i).sum();
		int sumYpow2 = yPow2.stream().mapToInt(i->i).sum();

		return (dataSetSize*sumXY - sumX*sumY) / Math.sqrt((dataSetSize*sumXpow2-sumX*sumX)*(dataSetSize*sumYpow2-sumY*sumY));
		
	}

}
