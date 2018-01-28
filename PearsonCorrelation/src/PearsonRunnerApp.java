import java.util.stream.Collectors;
import java.util.stream.Stream;

import ro.cs.ubbcluj.domain.Entity;
import ro.cs.ubbcluj.domain.PearsonCorrelation;
import ro.cs.ubbcluj.domain.Population;
import ro.cs.ubbcluj.domain.PopulationPearsonCorrelation;
import ro.cs.ubbcluj.domain.Variable;

public class PearsonRunnerApp {

	public static void main(String[] args) {
		Stream<Integer> stream = Stream.of(43, 21, 25, 42, 57, 59);
		Stream<Integer> stream2 = Stream.of(99, 65, 79, 75, 87, 81);

		Entity age = new Variable(stream.collect(Collectors.toList()));
		Entity glucoseLevel = new Variable(stream2.collect(Collectors.toList()));

		PearsonCorrelation r = new PearsonCorrelation(age.getFeatureList().size(), age, glucoseLevel);
		System.out.println(r.getPearsonCorrelation());
		
		//Pearson for a population
		Stream<Double> stream3 = Stream.of(2.1,2.5,3.6,4.0);
		Stream<Double>stream4 = Stream.of(8.0,10.0,12.0,14.0);
		Entity<Double> x = new Population(stream3.collect(Collectors.toList()));
		Entity<Double>y = new Population(stream4.collect(Collectors.toList()));
		PopulationPearsonCorrelation p2 = new PopulationPearsonCorrelation(x.getFeatureList().size(), x, y);
		
		System.out.println(p2.getPearsonCorrelationPopulation());

	}

}
