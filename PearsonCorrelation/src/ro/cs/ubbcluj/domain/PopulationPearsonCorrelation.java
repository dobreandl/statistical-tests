package ro.cs.ubbcluj.domain;

import java.util.ArrayList;
import java.util.List;

public class PopulationPearsonCorrelation {
	private int dataSetSize;
	private Entity<Double> x;
	private Entity<Double> y;

	public PopulationPearsonCorrelation(int dataSetSize, Entity x, Entity y) {
		super();
		this.dataSetSize = dataSetSize;
		this.x = x;
		this.y = y;
	}

	private Double computeMean(Entity<Double> e) {
		int sum = 0;

		for (Double value : e.getFeatureList()) {
			sum += value;
		}

		return (double) sum / e.getFeatureList().size();
	}

	/**
	 * Computes the standard deviation for an entity
	 * @param e with list of features
	 * @return standard deviation
	 */
	private Double getStandardDeviation(Entity<Double> e) {
		double mean = computeMean(e);
		List<Double> difference = new ArrayList<>();

		for (int i = 0; i < dataSetSize; i++) {
			difference.add(Math.abs(mean - e.getFeatureList().get(i)));
		}

		for (int i = 0; i < dataSetSize; i++) {
			Double value = difference.get(i);
			Double pow = value * value;
			difference.set(i, pow);
		}
		
		double sum = difference.stream().mapToDouble(i->i).sum();
		
		return Math.sqrt(sum/(dataSetSize-1));
	}

	private Double getCovariance(){
		List<Double>xValues = x.getFeatureList();
		List<Double>yValues = y.getFeatureList();
		double meanX = computeMean(x);
		double meanY = computeMean(y);
		double sum = 0;
		
		for(int i=0;i<dataSetSize;i++){
			double diff = (meanX-xValues.get(i))*(meanY-yValues.get(i));
			sum+=diff;
		}
		
		return sum / (dataSetSize-1);
	}
	
	public Double getPearsonCorrelationPopulation(){
		double covariance = getCovariance();
		double stdX = getStandardDeviation(x);
		double stdY = getStandardDeviation(y);
		return covariance/ (stdX*stdY);
	}
}
