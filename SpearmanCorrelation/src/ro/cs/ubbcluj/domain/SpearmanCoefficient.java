package ro.cs.ubbcluj.domain;

import java.util.ArrayList;
import java.util.List;

public class SpearmanCoefficient {
	private Entity<Integer> x;
	private Entity<Integer> y;
	private int dataSize;

	public SpearmanCoefficient(int dataSize, Entity<Integer> x, Entity<Integer> y) {
		super();
		this.x = x;
		this.y = y;
		this.dataSize = dataSize;
	}

	public double computeSpearmanWithoutTiedRanks() {
		List<Double> ranksX = x.computeRanks();
		List<Double> ranksY = y.computeRanks();
		List<Double> d = new ArrayList<>();

		System.out.println(ranksX);
		for (int i = 0; i < ranksX.size(); i++) {
			d.add(Math.abs(ranksX.get(i) - ranksY.get(i)));
		}

		for (int i = 0; i < d.size(); i++) {
			double value = d.get(i);
			d.set(i, value * value);
		}

		double sum = 0;
		for (double val : d) {
			sum += val;
		}

		System.out.println(sum);

		return 1 - ((6 * sum) / (dataSize * (dataSize * dataSize - 1)));

	}

	private double mean(Entity<Integer> variable) {
		double sum = 0.0;

		for (Double i : variable.computeRanks()) {
			sum += i;
		}

		return sum / variable. computeRanks().size();
	}

	public double computeSpearmanWithTiedRanks() {
		double xMean = mean(x);
		double yMean = mean(y);
		List<Double>diffX = new ArrayList<>();
		List<Double>diffY=new ArrayList<>();
		
		for(Double i:x.computeRanks()){
			diffX.add(Math.abs(i-xMean));
		}
		
		for(Double i:y.computeRanks()){
			diffY.add(Math.abs(i-yMean));
		}
		

		List<Double>product = new ArrayList<>();
		double sum =0.0;
		
		for(int i=0;i<diffX.size();i++){
			product.add(diffX.get(i)*diffY.get(i));
		}
		
		
		for(Double value:product){
			sum+=value;
		}
		
		System.out.println(sum);
		for(int i=0;i<diffX.size();i++){
			Double val = diffX.get(i);
			diffX.set(i, val*val);
		}
		
		double sumPow2=0.0;
		for(Double val:diffX){
			sumPow2+=val;
		}
		
		for(int i=0;i<diffY.size();i++){
			Double val = diffY.get(i);
			diffY.set(i, val*val);
		}
		
		double sumPow2Y=0.0;
		for(Double val:diffY){
			sumPow2Y+=val;
		}
		
		return sum / (Math.sqrt(sumPow2*sumPow2Y));
		
		
	}

}
