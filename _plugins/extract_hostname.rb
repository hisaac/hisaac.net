# frozen_string_literal: true

module Jekyll
  # Simple filter to extract the hostname from a given URL
  module ExtractHostname
    def extract_hostname(input)
      stripped_input = input.strip
      raise "The input to 'extact_hostname' was nil or empty" if stripped_input.nil? || stripped_input.empty?

      hostname = URI.parse(stripped_input).host
      raise "No valid hostname in #{input}" if hostname.nil? || hostname.empty?

      return hostname.sub(/\Awww\./, '')
    end
  end
end

Liquid::Template.register_filter(Jekyll::ExtractHostname)
