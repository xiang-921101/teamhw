from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# Configure the tracer provider
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Add a Console Exporter
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)
